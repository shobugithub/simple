from django.contrib import admin
from django.urls import path
from app.views import index_page, detail_product, add_product, add_comment, order_product, delete_product, edit_product

urlpatterns = [
    path('', index_page, name='index'),
    path('category/<int:cat_id>', index_page, name='category_by_id'),
    path('detail/<int:pk>', detail_product, name='detail'),
    path('add-product/', add_product, name='add_product'),
    path('detail/<int:product_id>/comment', add_comment, name='add_comment'),
    path('detail/<int:pk>/order', order_product, name='order_product'),

    path('detail/<int:pk>/delete-product', delete_product, name='delete'),
    path('detail/<int:pk>/edit-product', edit_product, name='edit'),

]
