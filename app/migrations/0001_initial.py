# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2016-10-13 12:54
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('username', models.CharField(max_length=80)),
                ('github_name', models.CharField(max_length=80)),
                ('alias', models.CharField(default=1, max_length=80)),
            ],
        ),
    ]
