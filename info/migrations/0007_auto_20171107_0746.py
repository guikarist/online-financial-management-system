# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-07 07:46
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('info', '0006_auto_20171107_0705'),
    ]

    operations = [
        migrations.AlterField(
            model_name='information',
            name='photo',
            field=models.ImageField(upload_to='photos/'),
        ),
    ]
