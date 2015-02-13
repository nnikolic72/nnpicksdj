# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('goodusers', '0008_auto_20150211_1619'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gooduser',
            name='instagram_profile_picture_URL',
            field=models.URLField(max_length=255, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='gooduser',
            name='instagram_user_website_URL',
            field=models.URLField(max_length=255, null=True, blank=True),
            preserve_default=True,
        ),
    ]
