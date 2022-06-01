from django.test import TestCase


# Create your tests here.

class CheckTemplates(TestCase):

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
