# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-07-28 01:51
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('assetmanager', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='asset',
            name='value',
            field=models.IntegerField(null=True),
        ),
    ]
