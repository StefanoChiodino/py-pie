# Generated by Django 2.0 on 2018-03-20 21:23

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('pie_run_order', '0002_auto_20180320_2057'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pierunorderentry',
            name='pie',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pie.Pie'),
        ),
    ]
