import requests
from django.contrib import messages
from django.contrib.auth import login, authenticate
from django.shortcuts import redirect, render
from django.views.generic import TemplateView, FormView, View
from .forms import SapanoUserCreateUser, SapanoUserLogin
from django.contrib.auth.forms import AuthenticationForm


# class COINData:

#     def __init__(self, sort, limit, currency):
#         self.cgk_url = f'https://api.coingecko.com/api/v3/coins/markets?vs_currency={currency}&order={sort}&' \
#                        f'per_page={limit}&page=1&sparkline=false'
#         self.tokpie_url = 'https://tokpie.com/api_ticker/?market=sapa@usdt'
#         self.ranks = requests.get(self.cgk_url).json()
#         self.sapa_price = requests.get(self.tokpie_url).json()


# RANKING_DATA = COINData(sort='market_cap_desc', limit=10, currency='usd')
# SAPA_PRICE = {key: value for key, value in RANKING_DATA.sapa_price['result'].items() if key == 'highestBid'}


# Create your views here.
class HomepageView(TemplateView):
    template_name = 'index.html'
    # extra_context = {'ranking': RANKING_DATA.ranks, 'company': 'Sapano Finance', 'sapa': SAPA_PRICE['highestBid']}

    def get_context_data(self, **kwargs):
        kwargs.setdefault('view', self)
        if self.extra_context is not None:
            kwargs.update(self.extra_context)
        return kwargs


class StakeView(TemplateView):
    template_name = 'stake.html'
    # extra_context = {'company': 'Sapano Finance', 'sapa': SAPA_PRICE['highestBid']}


class P2PView(TemplateView):
    template_name = 'p2p.html'
    # extra_context = {'company': 'Sapano Finance', 'sapa': SAPA_PRICE['highestBid']}


class EPOSView(TemplateView):
    template_name = 'epos.html'
    # extra_context = {'company': 'Sapano Finance', 'sapa': SAPA_PRICE['highestBid']}


class RegisterView(FormView):
    template_name = 'user/register.html'
    form_class = SapanoUserCreateUser
    success_url = '/Success URL/'
    # extra_context = {'company': 'Sapano Finance', 'sapa': SAPA_PRICE['highestBid']}

    def form_valid(self, form):
        response = super().form_valid(form)

        if form.is_valid():
            user = form.save()
            login(user)
            messages.success("Welcome to SapaNO Finance")
            return response
        else:
            messages.error("Please try again. Invalid information")


class SapanoLoginView(View):
    template_name = 'user/login.html'
    form_class = SapanoUserLogin
    next_page = 'index.html'

    def get(self, request):
        form = self.form_class()
        message = ''
        
        return render(request, template_name=self.template_name, context={'form': form, 'message': message})

    def post(self, request):
        form = self.form_class(request.POST)

        if form.is_valid():
            user = authenticate(username=form.cleaned_data['username'],
            password=form.cleaned_data['password'])
            if user is not None:
                login(request, user)
                print(user)
                return self.next_page

        message = 'Wrong details provided'
        return render(request, self.template_name, context={'form': form, 'message': message})
            


# def register(request):
#     if request.method == "POST":
#         form = SapanoUserCreateUser(request.POST)
#         if form.is_valid():
#             user = form.save()
#             login(request, user)
#             messages.success(request, "Welcome to SapaNO Finance")
#             return redirect("homepage")
#         messages.error(request, "Please try again. Invalid information")

#     form = SapanoUserCreateUser()
#     return render(request=request, template_name="user/register.html", context={"register_form": form})
