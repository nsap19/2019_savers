from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('',views.product,name="product"),
<<<<<<< HEAD
]

=======
    path('<int:pk>/detail', views.detail,name='detail'),
]
>>>>>>> 4ec8f3a956c12972e8d4aabf116ae74b5063b867
