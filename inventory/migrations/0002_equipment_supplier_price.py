# Generated by Django 5.1.4 on 2025-03-25 18:52

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Equipment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Supplier',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('contact_email', models.EmailField(max_length=254)),
            ],
        ),
        migrations.CreateModel(
            name='Price',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('date_added', models.DateTimeField(auto_now_add=True)),
                ('equipment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='prices', to='inventory.equipment')),
                ('supplier', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inventory.supplier')),
            ],
        ),
    ]
