# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-08-02 12:33
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0007_auto_20160802_0739'),
    ]

    operations = [
        migrations.AlterField(
            model_name='modules',
            name='status',
            field=models.CharField(choices=[('Niet gedaan', 'Niet gedaan'), ('Bezig', 'Bezig'), ('Voltooid', 'Voltooid')], default='Niet gedaan', max_length=15),
        ),
    ]