import knox.auth
from django.urls import path
from .views import RegisterAPI
from . import views
from knox import views as knox_views
from .views import LoginAPI
from django.urls import path
urlpatterns = [
    path('books/',views.book_list,name='book_list'),
    path('books/upload',views.upload_book,name='book_list'),
    path('upload/',views.upload,name='upload'),
    path('',views.index,name='home'),
    path('profile/',views.profile,name='profile'),
    path('login_user/',views.login_user,name='login'),
    path('register_user/',views.register_user,name='register'),
    path('logout_user/',views.logout_user,name='logout'),
    path('api/register/', RegisterAPI.as_view(), name='register'),
    path('api/login/', LoginAPI.as_view(), name='login'),
    path('api/logout/', knox_views.LogoutView.as_view(), name='logout'),
    path('api/logoutall/', knox_views.LogoutAllView.as_view(), name='logoutall'),
]