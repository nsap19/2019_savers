from django.shortcuts import get_object_or_404, render, redirect
from iamport import Iamport

# Create your views here.
def pay(request):
        current_user_pk = request.user.id

        # # 테스트 용
        # iamport = Iamport(imp_key='imp_apikey', imp_secret='ekKoeW8RyKuT0zgaZsUtXXTLQ4AhPFW3ZGseDA6bkA5lamv9OqDMnxyeB9wqOsuO9W3Mx9YSJ4dTqJ3f')
        # # 상품 아이디로 결제 상품 조회
        # response = iamport.find(merchant_uid='pk')
        # # 상품 아이디로 가격 확인
        # iamport.is_paid(product_price, merchant_uid='pk')
        # payload = {
        # 'customer_uid': 'current_user_pk',
        # 'merchant_uid': '00000000',
        # 'amount': 5000,
        # }
        # try:
        #         response = iamport.pay_again(**payload)
        # except KeyError:
        #         # 필수 값이 없을때 에러 처리
        #         pass
        # except Iamport.ResponseError as e:
        #         # 응답 에러 처리
        #         pass
        # except Iamport.HttpError as http_error:
        #         # HTTP not 200 응답 에러 처리
        #         pass


        return render(request,'pay/pay.html')
