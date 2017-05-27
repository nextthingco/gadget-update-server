# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-05-26 23:30
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
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
        migrations.CreateModel(
            name='Manifest',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('version', models.CharField(max_length=30)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('description', models.TextField(default='')),
                ('compatible', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Update',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('signature', models.CharField(max_length=1024)),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='updates', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='manifest',
            name='update',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='manifest', to='deploy.Update'),
        ),
        migrations.AddField(
            model_name='artifact',
            name='manifest',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='artifacts', to='deploy.Manifest'),
        ),
    ]
