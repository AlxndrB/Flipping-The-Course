# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-08-02 06:47
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_auto_20160802_0630'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='modules',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='questions',
        ),
        migrations.AddField(
            model_name='modules',
            name='userprofile',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='main.UserProfile'),
        ),
    ]