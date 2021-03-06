from django.test import TestCase
from .views import RANKING_DATA
import requests


# Create your tests here.

class Check(TestCase):

    def test_home(self):
        response = self.client.get('/')
        return self.assertEqual(response.status_code, 200)

    def test_stake(self):
        response = self.client.get('/stake/')
        return self.assertEqual(response.status_code, 200)

    def test_epos(self):
        response = self.client.get('/epos/')
        return self.assertEqual(response.status_code, 200)

    def test_p2p(self):
        response = self.client.get('/p2p/')
        return self.assertEqual(response.status_code, 200)

    def test_sapa_price(self):
        response = requests.get(RANKING_DATA.tokpie_url)
        return self.assertEqual(response.status_code, 200)

    def test_ranking(self):
        response = requests.get(RANKING_DATA.cgk_url)
        return self.assertEqual(response.status_code, 200)
