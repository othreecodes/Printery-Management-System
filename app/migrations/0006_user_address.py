# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-08-02 06:21
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_auto_20170802_0646'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='address',
            field=models.TextField(null=True),
        ),
    ]
