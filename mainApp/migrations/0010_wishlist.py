# Generated by Django 3.1.7 on 2021-04-13 12:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mainApp', '0009_auto_20210413_1727'),
    ]

    operations = [
        migrations.CreateModel(
            name='Wishlist',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('buyer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainApp.buyer')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainApp.product')),
            ],
        ),
    ]