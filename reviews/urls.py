from django.urls import path
from . import views
urlpatterns=[
    path('reviews',views.reviews,name='reviews'),
    path('review_create',views.review_create,name='review_create'),
    path('review/<int:pk>/update',views.review_update,name='review_update'),
    path('review/<int:pk>/delete',views.review_delete,name='review_delete'),
]