# Generated by Django 2.0.8 on 2018-11-28 15:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0013_auto_20181118_1442'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cart',
            name='user',
        ),
        migrations.RemoveField(
            model_name='entry',
            name='cart',
        ),
        migrations.RemoveField(
            model_name='entry',
            name='product',
        ),
        migrations.DeleteModel(
            name='Cart',
        ),
        migrations.DeleteModel(
            name='Entry',
        ),
    ]