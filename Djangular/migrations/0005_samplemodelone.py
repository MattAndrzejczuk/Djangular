# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-17 22:05
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Djangular', '0004_auto_20170717_1907'),
    ]

    operations = [
        migrations.CreateModel(
            name='SampleModelOne',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=75, unique=True)),
                ('description', models.TextField()),
            ],
        ),
    ]