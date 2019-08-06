from django.shortcuts import get_object_or_404, render, redirect
from product.models import *
from .models import *
from login.models import *



# Create your views here.
def mypage(request):
        return render(request,'mypage/mypage.html')

def mydetail(request):
        return render(request,'mypage/mydetail.html')

def addbasket(request,pk):
# def basket(request):
        baskets = Basket.objects
        
        if baskets.filter(user_id=1, product_id=pk).exists():
                basket = baskets.get(user_id=1, product_id=pk)
                basket.quantity +=1
                basket.save()
        else:
                # current_user_pk = request.user.id
                basket = Basket()
                # user = User(1)
                basket.user = User(1)
                basket.product = Product(pk)
                basket.status = 0
                basket.quantity =1
                
                basket.save()
        return redirect('/product')

def basket(request): #사용자 id를 pk로 넘기는것 나중에 추가
        products = Product.objects
        baskets = Basket.objects.all()
        u_basket = baskets.filter(user_id=1)


        return render(request, 'mypage/basket.html', {'products':products, 'baskets':baskets, 'u_basket':u_basket})


