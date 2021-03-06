# Generated by Django 4.0.6 on 2022-07-16 20:00

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('webapp', '0006_remove_orders_client_orders_user_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rate', models.FloatField()),
                ('order_type', models.CharField(choices=[('B', 'BUY'), ('S', 'SELL')], max_length=1)),
            ],
        ),
        migrations.CreateModel(
            name='P2POrder',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_type', models.CharField(choices=[('B', 'BUY'), ('S', 'SELL')], max_length=1)),
                ('token', models.CharField(choices=[('BTC', 'bitcoin'), ('ETH', 'etheruem'), ('XRP', 'ripple'), ('DOGE', 'dogecoin'), ('LTC', 'litecoin'), ('SHIB', 'shiba-inu'), ('BNB', 'binance-coin'), ('ADA', 'cardano'), ('MATIC', 'polygon-matic'), ('SAPA', 'sapano')], max_length=6)),
                ('available_tokens', models.IntegerField()),
                ('rate', models.FloatField()),
                ('amount', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='SapaNOUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Wallet',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('BTC', models.FloatField(default=0.0)),
                ('ETH', models.FloatField(default=0.0)),
                ('DOGE', models.FloatField(default=0.0)),
                ('XRP', models.FloatField(default=0.0)),
                ('LTC', models.FloatField(default=0.0)),
                ('SHIB', models.FloatField(default=0.0)),
                ('BNB', models.FloatField(default=0.0)),
                ('ADA', models.FloatField(default=0.0)),
                ('MATIC', models.FloatField(default=0.0)),
                ('SAPA', models.FloatField(default=0.0)),
            ],
        ),
        migrations.RemoveField(
            model_name='p2porders',
            name='user',
        ),
        migrations.RemoveField(
            model_name='wallets',
            name='user',
        ),
        migrations.DeleteModel(
            name='Orders',
        ),
        migrations.DeleteModel(
            name='P2POrders',
        ),
        migrations.DeleteModel(
            name='Wallets',
        ),
    ]
