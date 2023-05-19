from django.urls import path
from products.views import products, basket_add, basket_delete

app_name = 'products'

urlpatterns = [
    path('', products, name='index'), #../products/
    path('category/<int:category_id>', products, name='category'), #../products/category/<category_id>/
    path('page/<int:page_number>', products, name='paginator'), #../products/category/<category_id>/
    path('baskets/add/<int:product_id>/', basket_add, name='basket_add'), #../products/baskets/add/<product_id>/
    path('baskets/delete/<int:basket_id>/', basket_delete, name='basket_delete'), #../products/baskets/delete/<product_id>/
]
