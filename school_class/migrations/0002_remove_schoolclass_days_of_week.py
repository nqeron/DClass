# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-10-03 22:47
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('school_class', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='schoolclass',
            name='days_of_week',
        ),
    ]