# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('friends', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='friend',
            name='iconosquare_user_profile_page_URL',
            field=models.URLField(default=b'', max_length=255, null=True, blank=True),
            preserve_default=True,
        ),
    ]
