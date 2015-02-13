# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('goodusers', '0009_auto_20150212_1433'),
    ]

    operations = [
        migrations.AddField(
            model_name='gooduser',
            name='is_user_active',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='gooduser',
            name='to_be_processed',
            field=models.BooleanField(default=True),
            preserve_default=True,
        ),
    ]
