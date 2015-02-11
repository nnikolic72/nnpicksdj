# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('goodusers', '0007_gooduser_instagram_user_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='gooduser',
            name='instagram_profile_picture_URL',
            field=models.CharField(max_length=255, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='gooduser',
            name='instagram_user_bio',
            field=models.CharField(max_length=500, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='gooduser',
            name='instagram_user_website_URL',
            field=models.CharField(max_length=255, null=True, blank=True),
            preserve_default=True,
        ),
    ]
