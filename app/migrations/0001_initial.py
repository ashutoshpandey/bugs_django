# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Bug',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('description', models.CharField(max_length=1000)),
                ('severity', models.CharField(max_length=255)),
                ('status', models.CharField(max_length=50)),
                ('created_at', models.DateTimeField(verbose_name='created_at')),
            ],
        ),
        migrations.CreateModel(
            name='BugComment',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('comment', models.CharField(max_length=1000)),
                ('status', models.CharField(max_length=50)),
                ('created_at', models.DateTimeField(verbose_name='created_at')),
            ],
        ),
        migrations.CreateModel(
            name='BugCommentFile',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('file_name', models.CharField(max_length=255)),
                ('saved_file_name', models.CharField(max_length=255)),
                ('status', models.CharField(max_length=50)),
                ('created_at', models.DateTimeField(verbose_name='created_at')),
            ],
        ),
        migrations.CreateModel(
            name='BugFile',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('file_name', models.CharField(max_length=255)),
                ('saved_file_name', models.CharField(max_length=255)),
                ('status', models.CharField(max_length=50)),
                ('created_at', models.DateTimeField(verbose_name='created_at')),
            ],
        ),
        migrations.CreateModel(
            name='BugUser',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('status', models.CharField(max_length=50)),
                ('created_at', models.DateTimeField(verbose_name='created_at')),
            ],
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('description', models.CharField(max_length=1000)),
                ('status', models.CharField(max_length=50)),
                ('created_at', models.DateTimeField(verbose_name='created_at')),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('email', models.CharField(max_length=255)),
                ('password', models.CharField(max_length=255)),
                ('user_type', models.CharField(max_length=255)),
                ('profile_image_name', models.CharField(max_length=255)),
                ('profile_image_saved_name', models.CharField(max_length=255)),
                ('status', models.CharField(max_length=50)),
                ('created_at', models.DateTimeField(verbose_name='created_at')),
            ],
        ),
    ]
