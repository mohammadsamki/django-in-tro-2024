from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth.decorators import login_required

from .models import Product

# Create your views here.


@login_required(login_url='/store/account/login/')
def products(request):
    products = Product.objects.all()
    print(products)
    context = {'products':products}
    return render(request, 'products.html', context)


@login_required(login_url='/store/account/login/')
def home(request):
    numberOfVisit = request.session.get('numberOfVisit', 0)
    request.session['numberOfVisit'] = numberOfVisit + 1
    context = {'userName': 'Samaki'}
    context['number'] = numberOfVisit
    return render(request, 'home.html', context)


def product_detail(request, pk):
    product = get_object_or_404(Product, pk=pk)
    context = {'product': product}
    return render(request, 'product_detail.html', context)


def logout(request):
    request.session.flush()
    return redirect('/store/account/login/')

