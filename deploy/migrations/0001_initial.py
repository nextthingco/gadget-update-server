# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-05-26 00:31
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Artifact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('target', models.CharField(max_length=100)),
                ('type', models.CharField(max_length=100)),
                ('size', models.IntegerField()),
                ('checksum', models.CharField(max_length=64)),
                ('uri', models.CharField(max_length=256)),
            ],
            options={
                'ordering': ('uri',),
            },
        ),
    ]
