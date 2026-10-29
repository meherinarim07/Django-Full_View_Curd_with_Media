from django.urls import path
from . import views
urlpatterns=[
    path('products',views.products,name='products'),
    path('product_create',views.product_create,name='product_create'),
    path('product/<int:pk>/update',views.product_update,name='product_update'),
    path('product/<int:pk>/delete',views.product_delete,name='product_delete'),
]