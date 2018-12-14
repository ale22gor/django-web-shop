# Generated by Django 2.0.9 on 2018-12-14 10:47

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Adress',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('city', models.CharField(blank=True, max_length=250, null=True)),
                ('street', models.CharField(blank=True, max_length=250, null=True)),
                ('house', models.CharField(blank=True, max_length=250, null=True)),
                ('flat', models.CharField(blank=True, max_length=250, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254)),
                ('paid', models.BooleanField(default=False)),
                ('created', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated', models.DateTimeField(auto_now=True, null=True)),
                ('user', models.ForeignKey(blank=True, null=True, on_delete='Protect', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='OrderItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField()),
                ('created', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated', models.DateTimeField(auto_now=True, null=True)),
                ('order', models.ForeignKey(blank=True, null=True, on_delete='Cascade', related_name='items', to='order.Order')),
                ('product', models.ForeignKey(blank=True, null=True, on_delete='Protect', related_name='product_items', to='products.Product')),
            ],
        ),
        migrations.AddField(
            model_name='adress',
            name='order',
            field=models.OneToOneField(blank=True, null=True, on_delete='Cascade', related_name='order', to='order.Order'),
        ),
        migrations.CreateModel(
            name='OrderSummary',
            fields=[
            ],
            options={
                'verbose_name_plural': 'Orders Summary',
                'indexes': [],
                'proxy': True,
                'verbose_name': 'Order Summary',
            },
            bases=('order.orderitem',),
        ),
    ]
