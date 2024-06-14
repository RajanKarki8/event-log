
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('create/', views.create_event, name='create_event'),
    path('update/<str:event_id>/', views.update_event, name='update_event'),
    path('delete/<str:event_id>/', views.delete_event, name='delete_event'),
]
