from django.urls import path
from . import views

app_name = 'Shop'
urlpatterns = [
    path('', views.shop_list, name="shop_list"),
    path('<int:id>', views.shop_detail, name="shop_detail"),

]   