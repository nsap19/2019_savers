from django.shortcuts import get_object_or_404, render, redirect
from .models import *


# Create your views here.
#원하는 결과
# {'2':['길이':['21cm','24cm'],['색깔':['실버','블랙']]], '3':['길이':['23cm', '26cm']]}
def product(request):
    products = Product.objects.all()
    properties = ProductProperty.objects.all()
    propertynames = PropertyName.objects.all()
    grouped = dict()
    grouped2 = dict() 
    
    for obj in properties:
        pname = obj.property.property_name
        pid = obj.product_id
        pvalue = obj.property_value
        
        grouped2.setdefault(pname, []).append(pvalue)
        grouped.setdefault(pid, []).append(grouped2)
# {'길이': [['21cm', 2], ['24cm', 2], ['23cm', 3], ['26cm', 3]], '색깔': [['실버', 2], ['블랙', 2]]}


    # for obj in properties: 
    #     pid = obj.product_id
    #     pname = obj.property.property_name
    #     grouped.setdefault(pid, []).append(pname)
        
    #     pname = obj.property.property_name
    #     p = obj.property_value
    #     grouped2.setdefault(pname, []).append(p)
    #     # grouped2.setdefault(pname, []).append([p, pid])

    # for key, value in grouped.items(): #key= 물품id, value=속성이름    
    #     for k,val in grouped2.items(): #k=속성이름, val=속성 값,id
    #         if value == k:
    #             grouped[key][value].append(val[1])
    # {'길이': [2, 2, 3, 3, ['21cm', '24cm', '23cm', '26cm']], '색깔': [2, 2, ['실버', '블랙']]}

                

    # scorecard = {}
    # for st, score in zip(pname, p):
    #     scorecard[st] = dict(zip(pid,p))

    # for obj in properties.all():
    #     pname = obj.property.property_name
    #     p = obj.property_value
    #     grouped2.setdefault(grouped,[]).append(p)
    # current_user_pk = request.user.id
    

    return render(request, 'product/product.html', {'products':products, 'properties':properties, 'propertynames':propertynames, 'grouped': grouped , 'grouped2': grouped2 })

    
def detail(request, pk):
    product = Product.objects.get(pk=pk)
    properties = ProductProperty.objects.filter(product_id=pk)
    propertynames = PropertyName.objects
    grouped = dict() 
    for obj in properties.all():
        # grouped.setdefault(obj.property, []).append([obj.property_value, obj.product.id])
        pname = obj.property.property_name
        grouped.setdefault(pname, []).append(obj.property_value)
    # current_user_pk = request.user.id
    return render(request, 'product/detail.html',{'product':product, 'properties':properties, 'grouped': grouped})

