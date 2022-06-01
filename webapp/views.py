from django.shortcuts import render
from django.views.generic import TemplateView


# Create your views here.
class HomepageView(TemplateView):
    template_name = 'index.html'


class StakeView(TemplateView):
    template_name = 'stake.html'


class P2PView(TemplateView):
    template_name = 'p2p.html'


class EPOSView(TemplateView):
    template_name = 'epos.html'
