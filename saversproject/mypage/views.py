from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required

# Create your views here.
from product.models import *
from .models import *
from login.models import *



# Create your views here.
@login_required
def mypage(request):
        usermodel = get_user_model().objects.get(id=request.user.id)#현재 로그인된 유저의 id값과 일치하는 user객체 가져오기
        return render(request,'mypage/mypage.html', {'user':usermodel})

def mydetail(request):
        return render(request,'mypage/mydetail.html')

def order(request):
        return render(request,'mypage/order.html')
def addbasket(request,pk):
# def basket(request):
        baskets = Basket.objects
        r_option = request.GET['property']

        
        if baskets.filter(user_id=1, product_id=pk, p_option=r_option).exists():
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
                basket.p_option = r_option
                
                basket.save()
        return redirect('/mypage/basket')

def basket(request): #사용자 id를 pk로 넘기는것 나중에 추가
        products = Product.objects
        baskets = Basket.objects.all()
        u_basket = baskets.filter(user_id=1)

        return render(request, 'mypage/basket.html', {'products':products, 'baskets':baskets, 'u_basket':u_basket})

def update_amount(request,pk):
        products = Product.objects
        baskets = Basket.objects.all()
        u_basket = baskets.filter(user_id=1)

        b = u_basket.get(product_id=pk)
        b.quantity = request.GET['quantity']
        b.save()
        
        return redirect('/mypage/basket')

def delete_basket(request, pk):
        products = Product.objects
        baskets = Basket.objects.all()
        u_basket = baskets.filter(user_id=1)

        b = u_basket.get(id=pk)
        b.delete()

        return redirect('/mypage/basket')

def order_all(request):
        products = Product.objects
        baskets = Basket.objects.all()
        u_basket = baskets.filter(user_id=1)
        user_order = UserOrder.objects

        for b in u_basket:
                b.status = 1
                b.save()

        order = UserOrder()
        # user = User(1)
        order.user = User(1)
        order.ordered_product = Product(pk)
        order.amount = 0
        order.order_status =1
                
        order.save()
        
