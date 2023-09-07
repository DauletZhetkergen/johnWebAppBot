from django.shortcuts import render
from main.models import Product,Category


def index(request):
    category = request.GET.get('category')
    if category == None:
        products = Product.objects.all()
    else:
        products = Product.objects.filter(category__name = category)


    categories = Category.objects.all()


    context = {
        'products':products,
        'categories':categories,
    }
    return render(request,'main/index.html',context=context)