# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-18 12:40
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pie', '0004_auto_20171118_1103'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pie',
            name='price',
            field=models.DecimalField(decimal_places=2, max_digits=12),
        ),
    ]
