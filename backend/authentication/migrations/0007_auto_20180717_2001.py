# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2018-07-17 20:01
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0006_auto_20180716_1013'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='type',
            field=models.CharField(choices=[('talent', 'talent'), ('client', 'client')], max_length=10),
        ),
    ]
