# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-20 01:03
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('radio', '0003_auto_20171114_2046'),
    ]

    operations = [
        migrations.AddField(
            model_name='song',
            name='play_count',
            field=models.IntegerField(default=0),
        ),
    ]
