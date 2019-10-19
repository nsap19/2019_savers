from django.shortcuts import get_object_or_404, render, redirect
from pay.models import *

# Create your views here.
def main(request):
        coins = Coin.objects
        return render(request,'main/main.html',{'coins':coins})

def load(request):
        return render(request,'main/loading.html')