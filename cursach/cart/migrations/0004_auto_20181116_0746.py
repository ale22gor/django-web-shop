# Generated by Django 2.0.8 on 2018-11-16 07:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0003_auto_20181116_0746'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cart',
            name='products',
            field=models.ManyToManyField(blank=True, to='cart.Entry'),
        ),
    ]
