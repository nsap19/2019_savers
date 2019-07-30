<<<<<<< HEAD
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('',views.login,name="login"),
    path('signup/',views.signup,name="signup"),
]

=======
# from django.contrib import admin
# from django.urls import path, include
# from django.conf import settings
# from django.conf.urls.static import static
# from . import views

# urlpatterns = [
#     path('',views.login,name="login"),
#     path('signup/',views.signup,name="signup"),
# ]
>>>>>>> 4ec8f3a956c12972e8d4aabf116ae74b5063b867
