# Generated by Django 2.0.8 on 2018-12-10 08:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0009_ordersummary'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='created',
        ),
        migrations.RemoveField(
            model_name='order',
            name='updated',
        ),
        migrations.AddField(
            model_name='orderitem',
            name='created',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='orderitem',
            name='updated',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
    ]
