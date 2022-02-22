from django.shortcuts import render
from django.shortcuts import render, HttpResponse, redirect
from django.template import loader
from django.contrib import messages
from django.core.paginator import Paginator
from django.contrib.auth.models import User, auth
from django.contrib.auth import login, get_user_model
from django.contrib.auth.forms import UserCreationForm
from .forms import Userform, ContactForm
from .models import Product
from datetime import datetime

def Home(request):
    return render(request, 'index-4.html')


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect("/")
        else:
            messages.error(request, 'invalid credentials')
            return redirect('register')
    else:
        return render(request, 'login.html')


def register(request):
   form = Userform()
   if request.method == 'POST':
       form = Userform(request.POST)
       if form.is_valid():
           form.save()
           return redirect('login')
   context = {'form':form}
   return render(request, 'register.html', context)

def logout(request):
    auth.logout(request)
    return redirect('/')
def product_list(request, choice):
    Produc = Product.objects.filter(choice=choice)
    paginator = Paginator(Produc, 5)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {'Products':page_obj, 'choice':choice}
    return render(request, 'category-list.html', context)
def product_page(request, name):
    product = Product.objects.get(Title=name)
    pro = Product.objects.filter(choice=product.choice)
    return render(request, 'product.html', {'product':product, 'pro':pro})

def about_us(request):
    return render(request, 'about.html')

def privacy_policy(request):
    return render(request, 'privacy.html')

def terms(request):
    return render(request, 'terms.html')

def affiliate_disclosure(request):
    return render(request, 'affiliate.html')

def our_services(request):
    return render(request, 'services.html')








