from django.shortcuts import render
from django.http import HttpResponse
from .models import product
from math import ceil
from .forms1 import prod_form
# Create your views here.
def index(request):
    # products=product.objects.all()
    # print(products)

    # params={'no_of_slides':nSlides,'range':range(1,nSlides),'product':products}
    # allprods=[[products,range(1,nSlides),nSlides],
    #           [products,range(1,nSlides),nSlides]]
    allprods = []
    catprods = product.objects.values('category','id')
    cats = {item['category'] for item in catprods}
    for cat in cats:
        prod=product.objects.filter(category=cat)
        n = len(prod)
        nSlides = n // 4 + ceil((n / 4) - (n // 4))
        allprods.append([prod,range(1,nSlides),nSlides])
    params={'allprods':allprods}
    return render(request,'shop/index.html',params)


def about(request):
    return render(request,"shop/about.html")
def test123(request):
    abc=list(range(100))
    print(abc)
    return render(request,"shop/test123.html",{'lists':abc})

def contact(request):
    return HttpResponse("we are at contact")

def tracker(request):
    return HttpResponse("we are at tracker")

def search(request):
    return HttpResponse("we are at search")

def productView(request):
    return HttpResponse("we are at product view")

def checkout(request):
    return HttpResponse("we are at checkout")

def product_details(request):
    if request.method=='POST':
        print('hi')
        form=prod_form(request.POST,request.FILES)
        if form.is_valid():
            print("valid")
            form.save()
        else:
            print('not valid')
        form=prod_form()
        return render(request,'shop/form.html',{'form':form,'name':'sanskar'})
    return render(request,'shop/form.html',{'name':'sanskar'})