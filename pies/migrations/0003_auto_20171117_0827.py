# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-17 08:27
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pies', '0002_auto_20171117_0645'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pierunorderentries',
            name='pie',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='pies.Pie'),
        ),
    ]
