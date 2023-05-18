from django.urls import path
from products.views import products, basket_add, basket_delete

app_name = 'products'

urlpatterns = [
    path('', products, name='index'), 
    path('baskets/add/<int:product_id>/', basket_add, name='basket_add'), #../products/baskets/add/<product_id>/
    path('baskets/delete/<int:basket_id>/', basket_delete, name='basket_delete'),
]
