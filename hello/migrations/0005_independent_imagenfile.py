# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-03-01 00:01
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hello', '0004_auto_20160211_1159'),
    ]

    operations = [
        migrations.AddField(
            model_name='independent',
            name='imagenFile',
            field=models.ImageField(blank=True, upload_to=b'images'),
        ),
    ]