# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-08-03 10:09
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone
import model_utils.fields


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0009_payment_paid'),
    ]

    operations = [
        migrations.CreateModel(
            name='Grant',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('amount', models.IntegerField(null=True)),
                ('date_requested', models.DateTimeField(auto_now=True)),
                ('granted', models.BooleanField(default=False)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]