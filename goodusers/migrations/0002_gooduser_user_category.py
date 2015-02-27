# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('categories', '0003_auto_20150226_1451'),
        ('goodusers', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='gooduser',
            name='user_category',
            field=models.ManyToManyField(to='categories.Category', null=True, blank=True),
            preserve_default=True,
        ),
    ]
