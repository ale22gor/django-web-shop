# Generated by Django 2.0.8 on 2018-12-10 22:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0011_auto_20181210_2150'),
    ]

    operations = [
        migrations.AlterField(
            model_name='adress',
            name='order',
            field=models.OneToOneField(blank=True, null=True, on_delete='Cascade', related_name='order', to='order.Order'),
        ),
    ]
