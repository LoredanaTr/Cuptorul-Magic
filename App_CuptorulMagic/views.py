from django.shortcuts import render, redirect
from django.contrib.auth import login
from App_CuptorulMagic.forms import ProductForm
from App_CuptorulMagic.models.product import Product
from os.path import splitext

def home_view(request):
    return render(request, template_name='App_CuptorulMagic/home.html')

def upload_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            product = form.save()
            return redirect('home')

    else:
        form = ProductForm()
    return render(request, template_name='App_CuptorulMagic/upload_product.html', context={'form':form})


def products_view(request):
    products = Product.objects.all()
    image_names = {}
    for product in products:
        if '/' in product.image.name:
            image_name_parts = product.image.name.split('/')
            print(f'image path: {image_name_parts}')
            info = splitext(image_name_parts[1])[0]
            print(info)
            image_names[product.id] = info
        else:
            image_names[product.id] = splitext(product.image.name)[0]
            print(f'image names product id:{image_names[product.id]}')

    context = {'products': products, 'image_names': image_names}
    return render(request, template_name='App_CuptorulMagic/products.html', context=context)

def product_view(request, product_id):
    product = Product.objects.get(id=product_id)
    return render(request, 'App_CuptorulMagic/product.html', {'product': product})

