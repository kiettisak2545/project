# Generated by Django 5.1.5 on 2025-02-06 10:04

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='depositslip',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('depositslip_number', models.CharField(max_length=25)),
                ('depositslip_date', models.DateField(blank=True, null=True)),
                ('deposit_total', models.IntegerField()),
                ('deposit_vat', models.IntegerField()),
                ('deposit_totalprice', models.IntegerField()),
                ('deposit_status', models.IntegerField()),
            ],
        ),
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
                ('totalPrice', models.IntegerField()),
                ('quotation_status', models.CharField(max_length=10)),
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
                ('bank', models.CharField(max_length=25)),
                ('bank_address', models.CharField(max_length=50)),
                ('accountnumber', models.CharField(max_length=15)),
                ('userid_card', models.CharField(max_length=15)),
            ],
        ),
        migrations.CreateModel(
            name='deposit_orders',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('deposit_ordername', models.CharField(max_length=25)),
                ('deposit_price', models.IntegerField()),
                ('depositslip', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='_deposit_order', to='pApp.depositslip')),
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
                ('quotation', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='orders', to='pApp.quotation')),
            ],
        ),
        migrations.AddField(
            model_name='depositslip',
            name='quotation',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='depositslips', to='pApp.quotation'),
        ),
        migrations.CreateModel(
            name='slips',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slip', models.ImageField(blank=True, null=True, upload_to='slips/')),
                ('deposit', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Dslips', to='pApp.depositslip')),
            ],
        ),
    ]
