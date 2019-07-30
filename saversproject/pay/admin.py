from django.contrib import admin
<<<<<<< HEAD

# Register your models here.
=======
from .models import *


# Register your models here.
class PayAdmin(admin.ModelAdmin):
    list_display = ['id','buyer_name','amount']

admin.site.register(Pay,PayAdmin)
>>>>>>> 4ec8f3a956c12972e8d4aabf116ae74b5063b867
