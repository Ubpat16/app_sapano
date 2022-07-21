from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from .forms import SapanoUserCreateUser, SapanoUserLogin
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from .models import Wallet, P2POrder
from django.views.generic.base import TemplateView
from django.views.generic.list import ListView


@method_decorator(login_required, name='dispatch')
class HomepageView(TemplateView):
    template_name: str = 'index.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['wallet'] = Wallet
        context['company'] = 'Sapano Finance'
        return context


@method_decorator(login_required, name='dispatch')
class P2PView(TemplateView):
    template_name: str = 'p2p.html'
    model = P2POrder
    context = {
        'company': 'Sapano Finance'
    }
    

@method_decorator(login_required, name='dispatch')
class EPOSView(TemplateView):
    template_name: str = 'epos.html'
    context = {
        'company': 'Sapano Finance',
        'p2p_categories': P2POrder
    }
    

@method_decorator(login_required, name='dispatch')
class StakeView(TemplateView):
    template_name: str = 'stake.html'


class WalletView(ListView):
    model = Wallet
    # context_object_name = 'wallet'
    template_name = 'wallet.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['company'] = 'Sapano Finance'
        # context['wallet'] = Wallet
        return context


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
