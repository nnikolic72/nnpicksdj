# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('goodusers', '0010_auto_20150213_1234'),
    ]

    operations = [
        migrations.AddField(
            model_name='gooduser',
            name='iconosquare_user_profile_page_URL',
            field=models.URLField(default=b'', max_length=255, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='gooduser',
            name='instagram_user_profile_page_URL',
            field=models.URLField(default=b'', max_length=255, null=True, blank=True),
            preserve_default=True,
        ),
    ]
