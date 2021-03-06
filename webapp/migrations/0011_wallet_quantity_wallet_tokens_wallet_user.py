# Generated by Django 4.0.6 on 2022-07-21 04:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0010_remove_wallet_ada_remove_wallet_bnb_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='wallet',
            name='quantity',
            field=models.FloatField(default=0.0),
        ),
        migrations.AddField(
            model_name='wallet',
            name='tokens',
            field=models.CharField(choices=[('BTC', 'bitcoin'), ('ETH', 'etheruem'), ('XRP', 'ripple'), ('DOGE', 'dogecoin'), ('LTC', 'litecoin'), ('SHIB', 'shiba-inu'), ('BNB', 'binance-coin'), ('ADA', 'cardano'), ('MATIC', 'polygon-matic'), ('SAPA', 'sapano')], default=None, max_length=15),
        ),
        migrations.AddField(
            model_name='wallet',
            name='user',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='webapp.sapanouser'),
        ),
    ]
