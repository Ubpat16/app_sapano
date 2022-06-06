import requests
from django.views.generic import TemplateView


class COINData:

    def __init__(self, sort, limit, currency):
        self.cgk_url = f'https://api.coingecko.com/api/v3/coins/markets?vs_currency={currency}&order={sort}&' \
                       f'per_page={limit}&page=1&sparkline=false'
        self.tokpie_url = 'https://tokpie.com/api_ticker/?market=sapa@usdt'
        self.ranks = requests.get(self.cgk_url).json()
        self.sapa_price = requests.get(self.tokpie_url).json()


RANKING_DATA = COINData(sort='market_cap_desc', limit=10, currency='usd')
SAPA_PRICE = {key: value for key, value in RANKING_DATA.sapa_price['result'].items() if key == 'highestBid'}


# Create your views here.
class HomepageView(TemplateView):
    template_name = 'index.html'
    extra_context = {'ranking': RANKING_DATA.ranks, 'company': 'Sapano Finance', 'sapa': SAPA_PRICE['highestBid']}

    def get_context_data(self, **kwargs):
        kwargs.setdefault('view', self)
        if self.extra_context is not None:
            kwargs.update(self.extra_context)
        return kwargs


class StakeView(TemplateView):
    template_name = 'stake.html'
    extra_context = {'company': 'Sapano Finance', 'sapa': SAPA_PRICE['highestBid']}


class P2PView(TemplateView):
    template_name = 'p2p.html'
    extra_context = {'company': 'Sapano Finance', 'sapa': SAPA_PRICE['highestBid']}


class EPOSView(TemplateView):
    template_name = 'epos.html'
    extra_context = {'company': 'Sapano Finance', 'sapa': SAPA_PRICE['highestBid']}
