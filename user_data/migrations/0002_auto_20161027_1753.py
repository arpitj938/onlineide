# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-10-27 17:53
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_data', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user_data',
            name='roll_no',
            field=models.DecimalField(decimal_places=0, max_digits=10, unique=True),
        ),
    ]