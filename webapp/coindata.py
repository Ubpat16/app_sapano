import requests


class COINData:

    def __init__(self, sort, limit, currency):
        self.url = f'https://api.coingecko.com/api/v3/coins/markets?vs_currency={currency}&order={sort}&' \
                   f'per_page={limit}&page=1&sparkline=false'
        self.response = requests.get(self.url)

    def data(self):
        data = requests.get(self.url)
        return data.json()
