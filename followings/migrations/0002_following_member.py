# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0004_auto_20150306_1012'),
        ('followings', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='following',
            name='member',
            field=models.ManyToManyField(to='members.Member', null=True, blank=True),
            preserve_default=True,
        ),
    ]
