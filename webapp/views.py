from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import SapanoUserCreateUser, SapanoUserLogin
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from .models import Wallet

@login_required(login_url='user_login')
def homepage(request):
    home = 'index.html'
    context = {
        'company': 'Sapano Finance',
        'wallet': Wallet
        }
    return render(request, template_name=home, context=context)

@login_required(login_url='user_login')
def p2p(request):
    context = {
        'company': 'Sapano Finance'
        }
    p2p = 'p2p.html'
    return render(request, template_name=p2p, context=context)

@login_required(login_url='user_login')
def epos(request):
    epos = 'epos.html'
    context = {
        'company': 'Sapano Finance'
    }
    return render(request, template_name=epos, context=context)

@login_required(login_url='user_login')
def stake(request):
    stake = 'stake.html'
    return render(request, template_name=stake)

def wallet_view(request):
    wallet = 'wallet.html'
    context = {
        'company': 'Sapano Finance',
        'wallet': Wallet
    }
    return render(request, template_name=wallet, context=context)

def registeruser(request):
    form = SapanoUserCreateUser()
    register_template = 'user/register.html'
    context = {
        'form': form, 
        'company': 'Sapano Finance'
        }

    if request.method == "POST":
        form = SapanoUserCreateUser(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            messages.success(request, f'Hi {user}, Welcome to sapaNO Finance')

            return redirect('user_login')

    return render(request, template_name=register_template, context=context)

def loginuser(request):
    login_template = 'user/login.html'
    form = SapanoUserLogin()
    context = {
        'form': form, 
        'company': 'Sapano Finance'
        }

    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.success(request, f'Username OR Password is not correct')
    return render(request, template_name=login_template, context=context)


def logoutuser(request):
    logout(request)
    return redirect('user_login')