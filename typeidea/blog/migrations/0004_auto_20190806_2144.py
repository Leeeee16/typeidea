# -*- coding: utf-8 -*-
# Generated by Django 1.11.22 on 2019-08-06 13:44
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_post_content_html'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='post',
            options={'ordering': ['-id'], 'verbose_name': '文章', 'verbose_name_plural': '文章'},
        ),
    ]