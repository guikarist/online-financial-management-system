# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-07 01:18
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Salary',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bonus', models.DecimalField(decimal_places=2, max_digits=12)),
                ('bonus_date', models.DateField()),
                ('amount', models.DecimalField(decimal_places=2, max_digits=12)),
                ('paid_method', models.TextField()),
            ],
        ),
    ]