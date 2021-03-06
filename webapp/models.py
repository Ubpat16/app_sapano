from django.db import models
from django.contrib.auth.models import User


ORDER_TYPES = (
    ("B", 'BUY'),
    ("S", "SELL")
)

# SUPPORTED_TOKENS = (
#     ("BTC", "bitcoin"),
#     ("ETH", "etheruem"),
#     ("XRP", "ripple"),
#     ("DOGE", "dogecoin"),
#     ("LTC", "litecoin"),
#     ("SHIB", "shiba-inu"),
#     ("BNB", "binance-coin"),
#     ("ADA", "cardano"),
#     ("MATIC", "polygon-matic"),
#     ("SAPA", "sapano"),
# )

P2P_CATEGORY = (
    ('CM', 'Crypto Merchange'),
    ('FV', 'Food Vendor'),
    ('DP', 'Delivery Personnel'),
    ('HS', 'Hair Stylist'),
    ('MS', 'Mechanical Service'),
    ('MU', 'Music'),
    ('SM', 'Social Media Influencers'),
)
PAYMENT_METHOD = (
    ('TR', 'Bank Transfere'),
    ('CD', 'Card Payment'),
)
# Create your models here.


class SapaNOUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)


class Wallet(models.Model):
    user = models.ForeignKey(
        SapaNOUser, on_delete=models.CASCADE, default=None)
    tokens = models.CharField(max_length=15, default=None)
    quantity = models.FloatField(default=0.0)
    # BTC = models.FloatField(default=0.0)
    # ETH = models.FloatField(default=0.0)
    # DOGE = models.FloatField(default=0.0)
    # XRP = models.FloatField(default=0.0)
    # LTC = models.FloatField(default=0.0)
    # SHIB = models.FloatField(default=0.0)
    # BNB = models.FloatField(default=0.0)
    # ADA = models.FloatField(default=0.0)
    # MATIC = models.FloatField(default=0.0)
    # SAPA = models.FloatField(default=0.0)

    # def __str__(self) -> str:
    #     return self.wallet_address

    # @property
    # def wallet_balance(self):
    #     balance = self.BTC + self.ETH + self.DOGE + \
    #         self.XRP + self.LTC + self.SHIB + \
    #         self.ADA + self.MATIC + self.SAPA
    #     if balance == 0.0:
    #         return 0
    #     else:
    #         return balance

class P2POrder(models.Model):
    user = models.ForeignKey(
        SapaNOUser, on_delete=models.CASCADE, default=None)
    order_type = models.CharField(max_length=1, choices=ORDER_TYPES)
    token = models.CharField(max_length=6)
    category = models.CharField(max_length=2, choices=P2P_CATEGORY)
    payment = models.CharField(max_length=2, choices=PAYMENT_METHOD)
    available_tokens = models.IntegerField()
    rate = models.FloatField()
    amount = models.IntegerField()

    def __str__(self) -> str:
        return self.user.username


class Order(models.Model):
    order = models.ForeignKey(
        P2POrder, on_delete=models.CASCADE, default=None)
    rate = models.FloatField()
    order_type = models.CharField(max_length=1, choices=ORDER_TYPES)

    def __str__(self) -> str:
        return self.agent
