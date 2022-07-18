# Generated by Django 4.0.6 on 2022-07-14 20:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0004_orders_delete_eposorders_delete_sapatransactions_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='orders',
            old_name='agent',
            new_name='client',
        ),
        migrations.RemoveField(
            model_name='orders',
            name='available_tokens',
        ),
        migrations.AddField(
            model_name='p2porders',
            name='available_tokens',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='p2porders',
            name='rate',
            field=models.FloatField(default=0),
            preserve_default=False,
        ),
    ]
