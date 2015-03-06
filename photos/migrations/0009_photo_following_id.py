# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('followings', '0001_initial'),
        ('photos', '0008_photo_member_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='photo',
            name='following_id',
            field=models.ForeignKey(blank=True, to='followings.Following', null=True),
            preserve_default=True,
        ),
    ]
