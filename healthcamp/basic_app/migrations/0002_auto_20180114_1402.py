# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2018-01-14 14:02
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('basic_app', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='village',
            old_name='village_name',
            new_name='name',
        ),
    ]
