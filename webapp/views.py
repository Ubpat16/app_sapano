import requests
from django.views.generic import TemplateView
from .coindata import COINData

URL = 'https://tokpie.com/api_ticker/?market=sapa@usdt'
sapa = requests.get(URL).json()
sapa_price = {key: value for key, value in sapa['result'].items() if key == 'highestBid'}

RANKING = COINData(sort='market_cap_desc', limit=10, currency='usd')
CONTEXT = {'ranking': RANKING.data(), 'company': 'Sapano Finance', 'sapa': sapa_price['highestBid']}


# Create your views here.
class HomepageView(TemplateView):
    template_name = 'index.html'
    extra_context = CONTEXT

    def get_context_data(self, **kwargs):
        kwargs.setdefault('view', self)
        if self.extra_context is not None:
            kwargs.update(self.extra_context)
        return kwargs


class StakeView(TemplateView):
    template_name = 'stake.html'
    extra_context = CONTEXT


class P2PView(TemplateView):
    template_name = 'p2p.html'
    extra_context = CONTEXT


class EPOSView(TemplateView):
    template_name = 'epos.html'
    extra_context = CONTEXT
