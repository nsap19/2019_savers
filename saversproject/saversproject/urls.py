"""saversproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
<<<<<<< HEAD
=======
from django.conf import settings
from django.conf.urls.static import static
>>>>>>> 4ec8f3a956c12972e8d4aabf116ae74b5063b867

urlpatterns = [
    path('admin/', admin.site.urls),
    #go to main app (first page) 
<<<<<<< HEAD
    path('', include('main.urls')),
    #go to board app
    path('board/',include('board.urls')),
    #go to login app
    path('login/',include('login.urls')),
    #go to mypage app
    path('mypage/',include('mypage.urls')),
    #go to pay app
    path('pay/',include('pay.urls')),
    #go to product app
    path('product/',include('product.urls')),
]
=======
    # path('', include('main.urls')),
    # #go to board app
    # path('board/',include('board.urls')),
    # #go to login app
    # path('login/',include('login.urls')),
    # #go to mypage app
    # path('mypage/',include('mypage.urls')),
    # #go to pay app
    # path('pay/',include('pay.urls')),
    #go to product app
    path('product/',include('product.urls')),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
>>>>>>> 4ec8f3a956c12972e8d4aabf116ae74b5063b867
