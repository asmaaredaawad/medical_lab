# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-08-27 15:54
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tahleel', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patient',
            name='national_id',
            field=models.IntegerField(default='0', unique=True),
        ),
    ]
