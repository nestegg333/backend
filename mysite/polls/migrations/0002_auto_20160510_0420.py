# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-05-10 04:20
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='owner',
            name='lastPay',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
    ]
