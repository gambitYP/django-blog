# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-08-24 22:14
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_auto_20160822_1643'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='logo',
            field=models.FileField(default=2, upload_to=''),
            preserve_default=False,
        ),
    ]