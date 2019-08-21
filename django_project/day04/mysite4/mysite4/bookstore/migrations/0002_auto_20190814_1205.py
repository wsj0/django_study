# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2019-08-14 12:05
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookstore', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, verbose_name='姓名')),
                ('age', models.IntegerField(default=1, verbose_name='年龄')),
                ('email', models.EmailField(max_length=100, null=True, verbose_name='邮箱')),
            ],
        ),
        migrations.RemoveField(
            model_name='book',
            name='price',
        ),
        migrations.AddField(
            model_name='book',
            name='price1',
            field=models.DecimalField(decimal_places=2, max_digits=7, null=True, verbose_name='定价'),
        ),
        migrations.AddField(
            model_name='book',
            name='price2',
            field=models.DecimalField(decimal_places=2, max_digits=7, null=True, verbose_name='零售价'),
        ),
        migrations.AlterField(
            model_name='book',
            name='title',
            field=models.CharField(max_length=30, unique=True, verbose_name='书名'),
        ),
    ]
