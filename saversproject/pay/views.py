from django.shortcuts import get_object_or_404, render, redirect
# from iamport import Iamport

# Create your views here.
def pay(request):
        # current_user_pk = request.user.id

        # # 테스트 용
        # iamport = Iamport(imp_key='imp_apikey', imp_secret='('ekKoeW8RyKuT0zgaZsUtXXTLQ4AhPFW3ZGseDA6bkA5lamv9O''qDMnxyeB9wqOsuO9W3Mx9YSJ4dTqJ3f')')
        # # 상품 아이디로 조회
        # response = iamport.find(merchant_uid='{상품 아이디}')
        # iamport.is_paid(product_price, merchant_uid='{상품 아이디}')


        return render(request,'pay/pay.html')
