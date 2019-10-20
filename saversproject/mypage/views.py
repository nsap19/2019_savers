from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.utils import timezone


# Create your views here.
from product.models import *
from .models import *
from login.models import *



# Create your views here.
@login_required
def mypage(request):
        current_user_pk = request.user.id
        usermodel = get_user_model().objects.get(id=request.user.id)#현재 로그인된 유저의 id값과 일치하는 user객체 가져오기
        products = Product.objects
        baskets = Basket.objects
        u_basket = baskets.filter(user_id=current_user_pk)[:2]
        return render(request,'mypage/mypage.html', {'user':usermodel, 'u_basket':u_basket})

def mydetail(request):
        return render(request,'mypage/mydetail.html')

def ordercheck(request):
#         current_user_pk = request.user.id
#         products = Product.objects
#         baskets = Basket.objects.all()
#         user_order = UserOrder.objects.get(id=orderid)
#         u_basket = baskets.filter(user_id=current_user_pk)

#         # return redirect('ordercheck', id, user_order,u_basket)
        return 

def addbasket(request,pk):
        baskets = Basket.objects
        products = Product.objects
        r_option = ' '.join(request.GET.getlist('property[]'))
        current_user_pk = request.user.id
       
        
        if baskets.filter(user_id=current_user_pk, product_id=pk, p_option=r_option).exists():
                basket = baskets.get(user_id=current_user_pk, product_id=pk,p_option=r_option)
                basket.quantity +=1
                basket.save()
        else:
                basket = Basket()
                basket.user = User(current_user_pk)
                basket.product = Product(pk)
                basket.status = 0
                basket.quantity =1
                basket.p_option = r_option
                
                basket.save()
        return redirect('/mypage/basket')

def basket(request):
        current_user_pk = request.user.id
        products = Product.objects
        baskets = Basket.objects.all()
        u_basket = baskets.filter(user_id=current_user_pk)

        return render(request, 'mypage/basket.html', {'products':products, 'baskets':baskets, 'u_basket':u_basket})

def update_amount(request,pk):
        current_user_pk = request.user.id        
        products = Product.objects
        baskets = Basket.objects.all()
        u_basket = baskets.filter(user_id=current_user_pk)

        b = u_basket.get(product_id=pk)
        b.quantity = int(request.GET['quantity'])
        b.save()
        
        return redirect('/mypage/basket')

def delete_basket(request, pk):
        current_user_pk = request.user.id
        products = Product.objects
        baskets = Basket.objects.all()
        u_basket = baskets.filter(user_id=current_user_pk)

        b = u_basket.get(id=pk)
        b.delete()

        return redirect('/mypage/basket')

def order_all(request):
        current_user_pk = request.user.id
        products = Product.objects
        baskets = Basket.objects.all()
        u_basket = baskets.filter(user_id=current_user_pk)
        user_order = UserOrder.objects
        usermodel = get_user_model().objects.get(id=request.user.id)#현재 로그인된 유저의 id값과 일치하는 user객체 가져오기


        order = UserOrder()
        order.user = User(current_user_pk)

        for b in u_basket:
                b.status = 1
                order.ordered_product = b.product
                order.amount = b.quantity
                order.p_option = b.p_option
                b.save()
                
        order.order_status = OrderStatus(1)
        order.date = timezone.now()
        order.save()

        u_order =UserOrder.objects.filter(id=order.id)

        return render(request,'mypage/order_all.html', {'u_order':u_order, 'u_basket':u_basket, 'products':products, 'user':usermodel})


def order_complete(request):
        return render(request, 'mypage/order_complete.html')
        
