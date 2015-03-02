# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('friends', '0002_friend_iconosquare_user_profile_page_url'),
        ('photos', '0004_auto_20150301_1110'),
    ]

    operations = [
        migrations.AddField(
            model_name='photo',
            name='friend_id',
            field=models.ForeignKey(to='friends.Friend', null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='photo',
            name='good_user_id',
            field=models.ForeignKey(blank=True, to='goodusers.GoodUser', null=True),
            preserve_default=True,
        ),
    ]
