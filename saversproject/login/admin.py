from django.contrib import admin
<<<<<<< HEAD

# Register your models here.
=======
from .models import *


# Register your models here.
class UserAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'address', 'email', 'pw', 'tel', 'monthly_amount', 'donate_value','coin', 'post_code','term','use_period']

admin.site.register(User, UserAdmin)
>>>>>>> 4ec8f3a956c12972e8d4aabf116ae74b5063b867
