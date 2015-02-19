# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('goodusers', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='gooduser',
            options={'ordering': ('user_name',), 'get_latest_by': 'creation_date', 'verbose_name': 'Good User', 'verbose_name_plural': 'Good Users'},
        ),
        migrations.AddField(
            model_name='gooduser',
            name='iconosquare_user_profile_page_URL',
            field=models.URLField(default=b'', max_length=255, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='gooduser',
            name='instagram_profile_picture_URL',
            field=models.URLField(max_length=255, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='gooduser',
            name='instagram_user_bio',
            field=models.TextField(max_length=500, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='gooduser',
            name='instagram_user_id',
            field=models.CharField(max_length=100, unique=True, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='gooduser',
            name='instagram_user_name_valid',
            field=models.BooleanField(default=True, help_text='Check if Instagram user is valid/exists.'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='gooduser',
            name='instagram_user_profile_page_URL',
            field=models.URLField(default=b'', max_length=255, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='gooduser',
            name='instagram_user_website_URL',
            field=models.URLField(max_length=255, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='gooduser',
            name='is_user_active',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='gooduser',
            name='last_processed_date',
            field=models.DateTimeField(null=True, verbose_name=b'GoodUser processed date', blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='gooduser',
            name='times_processed',
            field=models.IntegerField(default=0, verbose_name=b'Number of times processed'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='gooduser',
            name='to_be_processed',
            field=models.BooleanField(default=True, help_text='Check if you want this Good User to be processed in the next Batch Run'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='gooduser',
            name='email',
            field=models.EmailField(max_length=75, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='gooduser',
            name='full_name',
            field=models.CharField(max_length=100, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='gooduser',
            name='instagram_user_full_name',
            field=models.CharField(max_length=100, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='gooduser',
            name='number_of_followers',
            field=models.IntegerField(default=0, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='gooduser',
            name='number_of_followings',
            field=models.IntegerField(default=0, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='gooduser',
            name='number_of_media',
            field=models.IntegerField(default=0, null=True, blank=True),
            preserve_default=True,
        ),
    ]
