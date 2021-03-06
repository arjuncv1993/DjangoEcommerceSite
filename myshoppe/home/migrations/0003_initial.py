# Generated by Django 4.0 on 2022-03-03 08:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('home', '0002_delete_itemlist'),
    ]

    operations = [
        migrations.CreateModel(
            name='itemlist',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Item_No', models.IntegerField()),
                ('Item_Name', models.CharField(max_length=50)),
                ('Brand', models.CharField(max_length=25)),
                ('Category', models.CharField(max_length=40)),
                ('Sub_Category', models.CharField(max_length=50)),
                ('Price', models.FloatField()),
                ('Features', models.TextField(max_length=200)),
            ],
        ),
    ]
