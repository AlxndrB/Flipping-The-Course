# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-08-05 11:20
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0011_modules_exp_required'),
    ]

    operations = [
        migrations.AddField(
            model_name='questions',
            name='userprofile',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='main.UserProfile'),
        ),
    ]
