"""Production app views"""
from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from .models import Item, Product, Production


# Dashboard
@login_required(login_url='user-login')
def dashboard(request):
    
    user_name = request.user.username
    items = Item.objects.order_by('-added')
    products = Product.objects.order_by('-added')
    productions = Production.objects.order_by('-added')
    
    context = {
        'user_name': user_name,
        'items': items,
        'products': products,
        'productions': productions
    }
    
    return render(request, 'production/dashboard.html', context=context)
