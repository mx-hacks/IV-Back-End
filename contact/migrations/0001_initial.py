# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-08-21 20:16
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Sponsor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('company', models.CharField(max_length=70)),
                ('message', models.TextField(blank=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('mail_sent', models.BooleanField(default=False)),
                ('message_id', models.CharField(max_length=400)),
            ],
            options={
                'ordering': ('-created',),
            },
        ),
    ]
