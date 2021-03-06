# Generated by Django 4.0.6 on 2022-07-13 22:14

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('webapp', '0003_rename_users_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='Orders',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rate', models.FloatField()),
                ('available_tokens', models.IntegerField()),
                ('order_type', models.CharField(choices=[('B', 'BUY'), ('S', 'SELL')], max_length=1)),
            ],
        ),
        migrations.DeleteModel(
            name='EPOSOrders',
        ),
        migrations.DeleteModel(
            name='SAPATransactions',
        ),
        migrations.DeleteModel(
            name='User',
        ),
        migrations.AddField(
            model_name='p2porders',
            name='amount',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='p2porders',
            name='order_type',
            field=models.CharField(choices=[('B', 'BUY'), ('S', 'SELL')], default=1, max_length=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='p2porders',
            name='token',
            field=models.CharField(choices=[('BTC', 'bitcoin'), ('ETH', 'etheruem'), ('XRP', 'ripple'), ('DOGE', 'dogecoin'), ('LTC', 'litecoin'), ('SHIB', 'shiba-inu'), ('BNB', 'binance-coin'), ('ADA', 'cardano'), ('MATIC', 'polygon-matic'), ('SAPA', 'sapano')], default=1, max_length=6),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='p2porders',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='orders',
            name='agent',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='webapp.p2porders'),
        ),
    ]
