from django.shortcuts import render
from product.models import *
from .models import *
from login.models import *


# Create your views here.
def mypage(request):
        return render(request,'mypage/mypage.html')

def mydetail(request):
        return render(request,'mypage/mydetail.html')

def basket(request,pk):
# def basket(request):

        # current_user_pk = request.user.id
        basket = Basket()
        # user = User(1)
        basket.user = User(1)
        basket.product = Product(pk)
        basket.status = 0
        basket.save()


        return render(request, 'mypage/basket.html')
