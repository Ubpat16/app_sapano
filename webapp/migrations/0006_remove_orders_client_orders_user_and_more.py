# Generated by Django 4.0.6 on 2022-07-16 01:17

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('webapp', '0005_rename_agent_orders_client_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='orders',
            name='client',
        ),
        migrations.AddField(
            model_name='orders',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='p2porders',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.CreateModel(
            name='Wallets',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('wallet_address', models.CharField(max_length=25)),
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
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]