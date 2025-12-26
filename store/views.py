from django.shortcuts import render, get_object_or_404
from .models import Category, Product

def home(request, category_slug=None):
    category_page = None
    products_list = None
    if category_slug != None:
        category_page = get_object_or_404(Category, slug=category_slug)
        products_list = Product.objects.filter(category=category_page, available=True)
    else:
        products_list = Product.objects.all().filter(available=True)
    return render(request, 'home.html', {'category': category_page, 'products': products_list})

def productPage(request, category_slug, product_slug):
    try:
        product = Product.objects.get(category__slug=category_slug, slug=product_slug)
    except Exception as e:
        raise e
    return render(request, 'product.html', {'product': product})

def cart(request):
    return render(request, 'cart.html')




