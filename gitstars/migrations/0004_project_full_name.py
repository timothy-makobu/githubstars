# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-17 12:23
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gitstars', '0003_auto_20161017_1201'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='full_name',
            field=models.CharField(default='octopus', max_length=255),
            preserve_default=False,
        ),
    ]