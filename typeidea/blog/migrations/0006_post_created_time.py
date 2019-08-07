# -*- coding: utf-8 -*-
# Generated by Django 1.11.22 on 2019-08-06 14:50
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_remove_post_created_time'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='created_time',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now, verbose_name='创建时间'),
            preserve_default=False,
        ),
    ]