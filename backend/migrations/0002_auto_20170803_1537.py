# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-08-03 07:37
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='SerialNumber',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('serials', models.CharField(default='null', max_length=200)),
                ('is_used', models.BooleanField(default=False)),
            ],
        ),
        migrations.AlterField(
            model_name='admin',
            name='email',
            field=models.EmailField(default='null', max_length=200),
        ),
        migrations.AlterField(
            model_name='admin',
            name='nickname',
            field=models.CharField(blank=True, default='null', max_length=100),
        ),
        migrations.AlterField(
            model_name='admin',
            name='password',
            field=models.CharField(blank=True, default='null', max_length=128),
        ),
        migrations.AlterField(
            model_name='chattinglog',
            name='client_id',
            field=models.CharField(blank=True, default='null', max_length=100),
        ),
        migrations.AlterField(
            model_name='chattinglog',
            name='content',
            field=models.CharField(blank=True, default='null', max_length=500),
        ),
        migrations.AlterField(
            model_name='chattinglog',
            name='service_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='backend.CustomerService'),
        ),
        migrations.AlterField(
            model_name='customerservice',
            name='email',
            field=models.EmailField(default='null', max_length=200),
        ),
        migrations.AlterField(
            model_name='customerservice',
            name='nickname',
            field=models.CharField(blank=True, default='null', max_length=100),
        ),
        migrations.AlterField(
            model_name='customerservice',
            name='password',
            field=models.CharField(blank=True, default='null', max_length=128),
        ),
    ]
