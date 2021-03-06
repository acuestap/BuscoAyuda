# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-02-10 04:39
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
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.CharField(blank=True, max_length=1000)),
                ('userEmail', models.CharField(blank=True, max_length=50)),
                ('created', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Independent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('imageFile', models.ImageField(null=True, upload_to=b'static/images')),
                ('yearsOfExperience', models.IntegerField(blank=True)),
                ('phoneNumber', models.CharField(blank=True, max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Job',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('jobName', models.CharField(blank=True, max_length=100)),
            ],
        ),
        migrations.AddField(
            model_name='independent',
            name='job',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='hello.Job'),
        ),
        migrations.AddField(
            model_name='independent',
            name='user',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='comment',
            name='independent',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='hello.Independent'),
        ),
    ]
