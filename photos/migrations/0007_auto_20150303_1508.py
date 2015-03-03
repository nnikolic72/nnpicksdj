# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('photos', '0006_auto_20150303_1350'),
    ]

    operations = [
        migrations.AlterField(
            model_name='photo',
            name='friend_id',
            field=models.ForeignKey(blank=True, to='friends.Friend', null=True),
            preserve_default=True,
        ),
    ]
