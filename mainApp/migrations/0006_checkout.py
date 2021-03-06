# Generated by Django 3.1.7 on 2021-03-31 15:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mainApp', '0005_cart'),
    ]

    operations = [
        migrations.CreateModel(
            name='Checkout',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('total', models.IntegerField()),
                ('name', models.CharField(default=None, max_length=20)),
                ('phone', models.CharField(default=None, max_length=20)),
                ('email', models.CharField(default=None, max_length=20)),
                ('address1', models.CharField(max_length=30)),
                ('address2', models.CharField(max_length=30)),
                ('city', models.CharField(max_length=30)),
                ('state', models.CharField(max_length=30)),
                ('pin', models.CharField(max_length=30)),
                ('mode', models.CharField(default=None, max_length=30)),
                ('cart', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainApp.cart')),
            ],
        ),
    ]
