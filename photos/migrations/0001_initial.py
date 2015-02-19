# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('goodusers', '0002_auto_20150219_0905'),
    ]

    operations = [
        migrations.CreateModel(
            name='Photo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('instagram_photo_id', models.CharField(max_length=255)),
                ('instagram_low_resolution_URL', models.URLField(max_length=255, null=True, blank=True)),
                ('instagram_thumbnail_URL', models.URLField(max_length=255, null=True, blank=True)),
                ('instagram_standard_resolution_URL', models.URLField(max_length=255, null=True, blank=True)),
                ('instagram_link_URL', models.URLField(max_length=255, null=True, blank=True)),
                ('instagram_caption', models.TextField(max_length=1000, null=True, blank=True)),
                ('instagram_tags', models.TextField(max_length=1000, null=True, blank=True)),
                ('instagram_created_time', models.CharField(max_length=100, null=True, blank=True)),
                ('instagram_photo_valid', models.BooleanField(default=True)),
                ('instagram_likes', models.IntegerField(default=0, null=True, blank=True)),
                ('instagram_comments', models.IntegerField(default=0, null=True, blank=True)),
                ('creation_date', models.DateTimeField(default=datetime.datetime(2015, 2, 19, 9, 5, 31, 663000), verbose_name=b'Photo creation date', auto_now_add=True)),
                ('last_update_date', models.DateTimeField(default=datetime.datetime(2015, 2, 19, 9, 5, 31, 663000), verbose_name=b'Photo last update date', auto_now=True)),
                ('good_user_id', models.ForeignKey(to='goodusers.GoodUser', null=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
