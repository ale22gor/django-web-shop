# Generated by Django 2.0.8 on 2018-12-08 10:44

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('comment', '0002_auto_20181208_0855'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='author',
            field=models.ForeignKey(on_delete='Protect', to=settings.AUTH_USER_MODEL),
        ),
    ]
