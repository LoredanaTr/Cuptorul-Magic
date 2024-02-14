from django.urls import path
from App_CuptorulMagic.views import home_view, contact, ProductListView, product_detail, upload_product, add_to_cart, delete_product, shopping_cart, finalizeaza_comanda
#in cadrul acestui fisier vom defini lista de app-pointuri a aplicatiei

app_name = "App_CuptorulMagic"


urlpatterns = [
    path('', home_view, name='home'),
    path('upload_product/', upload_product, name='upload_product'),
    path('products/', ProductListView.as_view(), name='products'),
    path('product/<int:product_id>/', product_detail, name='product'),
    path('cart/', shopping_cart, name='cart'),
    path('add_to_cart/<int:product_id>/', add_to_cart, name='add_to_cart'),
    path('delete_product/<int:product_id>/', delete_product, name='delete_product'),
    path('finalizeaza_comanda/', finalizeaza_comanda, name='finalizeaza_comanda'),
    path('contact/', contact, name='contact'),
]