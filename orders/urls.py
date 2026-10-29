from django.urls import path
from .import views
urlpatterns=[
    path('orders',views.orders,name='orders'),
    path('order/<int:pk>/create',views.order_create,name='order_create'),
    path('order/<int:pk>/update',views.order_update,name='order_update'),
    path('order/<int:pk>/delete',views.order_delete,name='order_delete'),
]