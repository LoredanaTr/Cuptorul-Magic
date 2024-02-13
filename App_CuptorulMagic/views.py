from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.urls import reverse
from App_CuptorulMagic.models import Product, Order, OrderItem
from django.views.generic import ListView
from django.db.models import F
from .forms import OrderItemForm, ProductForm, MesajForm



def home_view(request):
    return render(request, 'App_CuptorulMagic/home.html')


class ProductListView(ListView): # clasa cu ajutorul caruia afisam o lista de obiecte
    model = Product
    template_name = 'App_CuptorulMagic/products.html'

    def get_context_data(self, **kwargs): # metoda cu ajutorul caruia furnizam date suplimentare  catre sablon, pagina products.html
        context = super().get_context_data(**kwargs)
        context['products'] = context['object_list']
        return context


def product_detail(request, product_id): # functia care ne afiseaza informatii despre produs tinand cond de un id
    product = get_object_or_404(Product, pk=product_id)
    return render(request, 'App_CuptorulMagic/product.html', {'product': product})


def upload_product(request): # functie cu ajutorul caruia putem incarca produse in aplicatia noastra folosind un sablon, pagina upload_product.html
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            product = form.save()
            return redirect('/')
    else:
        form = ProductForm()

    return render(request, 'App_CuptorulMagic/upload_product.html', {'form': form})

@login_required
def add_to_cart(request, product_id): # functie cu ajutorul cauia putem adauga produse in cosul de cumparaturi
    try:
        # Obtine produsul pe baza id-ului
        product = get_object_or_404(Product, id=product_id)

        # Verificam daca exista deja un OrderItem pentru acest produs și utilizator
        order_item, created = OrderItem.objects.get_or_create(
            user=request.user,
            ordered=False,
            product=product
        )

        if created:
            messages.success(request, f"{product.name} a fost adăugat în coș.")
        else:
            # Daca OrderItem exista deja, vom actualiza cantitatea
            order_item.quantity = F('quantity') + 1
            order_item.save()
            messages.info(request, f"Cantitatea pentru {product.name} a fost actualizată în coș.")

        # Redirectionam catre pagina de shopping cart
        return redirect(reverse('sweet_market_place8_app:cart'))
    except Exception as e:
        # Putem gestiona eroarea si returnam un mesaj
        messages.error(request, f"Eroare la adăugarea produsului în coș: {str(e)}")
        return redirect('/')


@login_required
def create_order(request): # functie cu ajutorul cauia putem crea o comanda
    form = OrderItemForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            product_id = form.cleaned_data['product'].id
            quantity = form.cleaned_data['quantity']

            order_item, created = OrderItem.objects.get_or_create(
                user=request.user,
                ordered=False,
                product_id=product_id,
            )
            order_item.quantity += quantity
            order_item.save()

            return JsonResponse({'status': 'success'})

    order_items = OrderItem.objects.filter(user=request.user, ordered=False)
    order_total = sum(item.get_final_price() for item in order_items)

    context = {
        'form': form,
        'order_items': order_items,
        'order_total': order_total,
    }
    return render(request, 'App_CuptorulMagic/cart.html', context)


def finalizeaza_comanda(request):
    if request.method == 'POST':

        order_items = OrderItem.objects.filter(user=request.user, ordered=False)

        new_order = Order.objects.create(user=request.user, ordered=True)
        new_order.items.set(order_items)

        order_items.update(ordered=True)

        messages.success(request, 'Comanda a fost plasată cu succes!')
        return redirect(reverse('App_CuptorulMagic:home'))

    return redirect(reverse('App_CuptorulMagic:home'))


def shopping_cart(request):
    order_items = OrderItem.objects.filter(user=request.user, ordered=False)

    order_total = sum(item.get_final_price() for item in order_items)

    context = {
        'order_items': order_items,
        'total_cumparaturi': order_total,
    }

    return render(request, 'App_CuptorulMagic/cart.html', context)


@login_required
def delete_product(request, product_id):
    if request.method == 'DELETE':
        try:
            order_item = OrderItem.objects.get(user=request.user, product_id=product_id, ordered=False)
            order_item.delete()
            return JsonResponse({'status': 'success'})
        except OrderItem.DoesNotExist:
            return JsonResponse({'status': 'error', 'message': 'Produsul nu a fost găsit în coș'})
    else:
        return JsonResponse({'status': 'error', 'message': 'Metoda solicitată nu este permisă'})


def contact(request):
    if request.method == 'POST':
        form = MesajForm(request.POST)
        if form.is_valid():
            mesaj_nou = form.save(commit=False)
            mesaj_nou.status = 'necitit'
            mesaj_nou.save()
            return redirect('/')  # Redirectionam la pagina de home
    else:
        form = MesajForm()

    return render(request, 'App_CuptorulMagic/contact.html', {'form': form})



