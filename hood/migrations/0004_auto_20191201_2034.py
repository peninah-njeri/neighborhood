# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-12-01 17:34
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hood', '0003_category_comment_healthcenter_location_policecenters'),
    ]

    operations = [
        migrations.AddField(
            model_name='business',
            name='business_image',
            field=models.ImageField(null=True, upload_to='businesses'),
        ),
        migrations.AddField(
            model_name='neighborhood',
            name='neighborhood_image',
            field=models.ImageField(null=True, upload_to='neighborhoods'),
        ),
        migrations.AddField(
            model_name='post',
            name='post_image',
            field=models.ImageField(null=True, upload_to='posts'),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='profile_image',
            field=models.ImageField(null=True, upload_to='userprofiles'),
        ),
    ]
