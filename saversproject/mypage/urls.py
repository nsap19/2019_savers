from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from . import views

# app_name = "mypage_app"

urlpatterns = [
    path('',views.mypage,name="mypage"),
    path('mydetail/',views.mydetail,name="mydetail"),
    path('order/',views.order,name="order"),
    # path('<int:p_id>/basket', views.basket, name="basket"), 
    path('basket/<int:pk>/add', views.addbasket, name="addbasket"), 
    path('basket', views.basket, name = 'basket'),
    path('basket/amountupdate/<int:pk>',views.update_amount, name = 'amountupdate'),
    path('basket/deletebasket/<int:pk>', views.delete_basket, name = 'deletebasket'),
]

