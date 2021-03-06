# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-13 12:44
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0020_auto_20171110_0333'),
        ('salary', '0010_auto_20171113_0657'),
    ]

    operations = [
        migrations.RenameField(
            model_name='salary',
            old_name='staff',
            new_name='payee',
        ),
        migrations.RemoveField(
            model_name='salary',
            name='uploader',
        ),
        migrations.AddField(
            model_name='salary',
            name='payer',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='staff_who_pay_others', to='accounts.Staff'),
        ),
    ]
