# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2018-01-18 06:29
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0013_auto_20180118_0906'),
    ]

    operations = [
        migrations.AlterField(
            model_name='historicaltask',
            name='lasteditby',
            field=models.ForeignKey(blank=True, db_column='LastEditBy', db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='project.Employee', to_field='empid'),
        ),
    ]
