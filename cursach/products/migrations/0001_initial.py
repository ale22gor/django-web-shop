# Generated by Django 2.0.8 on 2018-11-14 10:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Film',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=64)),
                ('Amount', models.IntegerField()),
                ('Price', models.IntegerField()),
                ('Descr', models.TextField()),
            ],
        ),
    ]
