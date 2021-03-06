# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2018-03-05 00:33
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Quote',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('msg', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('aliasname', models.CharField(max_length=255)),
                ('email', models.CharField(max_length=255)),
                ('password', models.CharField(max_length=50)),
                ('birthdate', models.DateField()),
            ],
        ),
        migrations.AddField(
            model_name='quote',
            name='uploader',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='created_quotes', to='beltapp.User'),
        ),
        migrations.AddField(
            model_name='quote',
            name='userfavs',
            field=models.ManyToManyField(related_name='fav_quotes', to='beltapp.User'),
        ),
    ]
