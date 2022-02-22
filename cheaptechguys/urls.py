from django.urls import path
from  . import views
from django.contrib.auth import views as auth_view
urlpatterns = [
    path('', views.Home , name='Home'),
    path('login', views.login, name='login'),
    path('logout', views.logout, name='logout'),
    path('categorylist/<choice>', views.product_list, name='categorylist'),
    path('product/<name>', views.product_page, name='product'),
    path('register', views.register, name='register'),
    path('about us', views.about_us, name='about us'),
    path('affiliate disclosure', views.affiliate_disclosure, name='affiliate disclosure')
]