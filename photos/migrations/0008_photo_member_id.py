# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0003_member_user_type'),
        ('photos', '0007_auto_20150303_1508'),
    ]

    operations = [
        migrations.AddField(
            model_name='photo',
            name='member_id',
            field=models.ForeignKey(blank=True, to='members.Member', null=True),
            preserve_default=True,
        ),
    ]
