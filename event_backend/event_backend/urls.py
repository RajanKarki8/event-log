
from django.contrib import admin
from django.urls import path, include
from auth_user import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('main.urls')),
    path('login/',auth_views.Userlogin, name='login'),
    path('logout/', auth_views.Userlogout, name= 'logout'),
    path('register/',auth_views.UserRegister, name='register'),
]
