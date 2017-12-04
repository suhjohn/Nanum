# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-12-04 08:38
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0023_auto_20171204_1645'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='question',
            name='downvote_count',
        ),
        migrations.RemoveField(
            model_name='question',
            name='upvote_count',
        ),
        migrations.AddField(
            model_name='answer',
            name='bookmark_count',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='answer',
            name='downvote_count',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='answer',
            name='upvote_count',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='comment',
            name='downvote_count',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='comment',
            name='upvote_count',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='question',
            name='follow_count',
            field=models.IntegerField(default=0),
        ),
    ]
