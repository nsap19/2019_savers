from django.contrib import admin
<<<<<<< HEAD

# Register your models here.
=======
from .models import *

class UserOrderAdmin(admin.ModelAdmin):
    list_display = ['id', 'user','ordered_product','amount', 'date','order_status']

class BasketAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'product', 'status']

class DonationAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'product', 'donation_value']

class OrderStatusAdmin(admin.ModelAdmin):
    list_display = ['id', 'order_status']

# Register your models here.
admin.site.register(UserOrder, UserOrderAdmin)
admin.site.register(Basket, BasketAdmin)
admin.site.register(Donation, DonationAdmin)
admin.site.register(OrderStatus, OrderStatusAdmin)
>>>>>>> 4ec8f3a956c12972e8d4aabf116ae74b5063b867
