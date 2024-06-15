
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('create/', views.create_event, name='create_event'),
    path('update/<str:pk>/', views.update_event, name='update_event'),
    path('delete/<str:pk>/', views.delete_event, name='delete_event'),
]
