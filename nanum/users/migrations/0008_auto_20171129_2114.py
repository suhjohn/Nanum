# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-29 12:14
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0007_auto_20171126_1549'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='facebook_user_id',
            field=models.CharField(blank=True, max_length=300, verbose_name='facebook user id'),
        ),
    ]