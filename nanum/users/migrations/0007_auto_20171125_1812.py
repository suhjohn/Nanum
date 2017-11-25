# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-25 09:12
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0004_auto_20171125_1812'),
        ('users', '0006_auto_20171125_1346'),
    ]

    operations = [
        migrations.CreateModel(
            name='CommentDownVote',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('comment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='posts.Comment')),
            ],
        ),
        migrations.CreateModel(
            name='CommentUpVote',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('comment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='posts.Comment')),
            ],
        ),
        migrations.RemoveField(
            model_name='answercommentdownvote',
            name='baseanswercommentvote_ptr',
        ),
        migrations.RemoveField(
            model_name='answercommentupvote',
            name='baseanswercommentvote_ptr',
        ),
        migrations.AlterUniqueTogether(
            name='baseanswercommentvote',
            unique_together=set([]),
        ),
        migrations.RemoveField(
            model_name='baseanswercommentvote',
            name='comment',
        ),
        migrations.RemoveField(
            model_name='baseanswercommentvote',
            name='user',
        ),
        migrations.AlterUniqueTogether(
            name='basenestedcommentvote',
            unique_together=set([]),
        ),
        migrations.RemoveField(
            model_name='basenestedcommentvote',
            name='comment',
        ),
        migrations.RemoveField(
            model_name='basenestedcommentvote',
            name='user',
        ),
        migrations.AlterUniqueTogether(
            name='basequestioncommentvote',
            unique_together=set([]),
        ),
        migrations.RemoveField(
            model_name='basequestioncommentvote',
            name='comment',
        ),
        migrations.RemoveField(
            model_name='basequestioncommentvote',
            name='user',
        ),
        migrations.RemoveField(
            model_name='nestedcommentdownvote',
            name='basenestedcommentvote_ptr',
        ),
        migrations.RemoveField(
            model_name='nestedcommentupvote',
            name='basenestedcommentvote_ptr',
        ),
        migrations.RemoveField(
            model_name='questioncommentdownvote',
            name='basequestioncommentvote_ptr',
        ),
        migrations.RemoveField(
            model_name='questioncommentupvote',
            name='basequestioncommentvote_ptr',
        ),
        migrations.RemoveField(
            model_name='user',
            name='downvoted_answer_comments',
        ),
        migrations.RemoveField(
            model_name='user',
            name='downvoted_nested_comments',
        ),
        migrations.RemoveField(
            model_name='user',
            name='downvoted_question_comments',
        ),
        migrations.RemoveField(
            model_name='user',
            name='upvoted_answer_comments',
        ),
        migrations.RemoveField(
            model_name='user',
            name='upvoted_nested_comments',
        ),
        migrations.RemoveField(
            model_name='user',
            name='upvoted_question_comments',
        ),
        migrations.DeleteModel(
            name='AnswerCommentDownVote',
        ),
        migrations.DeleteModel(
            name='AnswerCommentUpVote',
        ),
        migrations.DeleteModel(
            name='BaseAnswerCommentVote',
        ),
        migrations.DeleteModel(
            name='BaseNestedCommentVote',
        ),
        migrations.DeleteModel(
            name='BaseQuestionCommentVote',
        ),
        migrations.DeleteModel(
            name='NestedCommentDownVote',
        ),
        migrations.DeleteModel(
            name='NestedCommentUpVote',
        ),
        migrations.DeleteModel(
            name='QuestionCommentDownVote',
        ),
        migrations.DeleteModel(
            name='QuestionCommentUpVote',
        ),
        migrations.AddField(
            model_name='commentupvote',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='commentdownvote',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='user',
            name='downvoted_comments',
            field=models.ManyToManyField(blank=True, related_name='downvoted_users', through='users.CommentDownVote', to='posts.Comment'),
        ),
        migrations.AddField(
            model_name='user',
            name='upvoted_comments',
            field=models.ManyToManyField(blank=True, related_name='upvoted_users', through='users.CommentUpVote', to='posts.Comment'),
        ),
        migrations.AlterUniqueTogether(
            name='commentupvote',
            unique_together=set([('user', 'comment')]),
        ),
        migrations.AlterUniqueTogether(
            name='commentdownvote',
            unique_together=set([('user', 'comment')]),
        ),
    ]
