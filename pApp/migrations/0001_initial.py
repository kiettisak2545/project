# Generated by Django 5.1.5 on 2025-01-22 07:48

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='quotation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.CharField(max_length=10)),
                ('url', models.CharField(blank=True, max_length=255, null=True)),
                ('date', models.DateField(blank=True, null=True)),
                ('name', models.CharField(max_length=25)),
                ('lastName', models.CharField(max_length=25)),
                ('address', models.CharField(max_length=50)),
                ('tel', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='user',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=25)),
                ('password', models.CharField(max_length=25)),
                ('name', models.CharField(max_length=25)),
                ('lastName', models.CharField(max_length=25)),
                ('address', models.CharField(max_length=50)),
                ('tel', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.IntegerField()),
                ('orderName', models.CharField(max_length=25)),
                ('price', models.IntegerField()),
                ('total', models.IntegerField()),
                ('totalPrice', models.IntegerField()),
                ('quotation', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='orders', to='pApp.quotation')),
            ],
        ),
    ]
