# -*- coding: utf-8 -*-
# Generated by Django 1.11.12 on 2018-06-06 17:27
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('boards', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='data',
            name='date',
            field=models.DateTimeField(),
        ),
    ]
