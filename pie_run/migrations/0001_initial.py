# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-18 11:04
from __future__ import unicode_literals

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PieRun',
            fields=[
                ('pie_run_id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('date', models.DateField()),
            ],
        ),
    ]
