from django.contrib import admin
from .models import P2POrder, Order, Wallet

# Register your models here.
admin.site.register(P2POrder)
admin.site.register(Order)
admin.site.register(Wallet)