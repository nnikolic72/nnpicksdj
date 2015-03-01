# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('photos', '0003_auto_20150301_1109'),
    ]

    operations = [
        migrations.AlterField(
            model_name='photo',
            name='creation_date',
            field=models.DateTimeField(auto_now_add=True, verbose_name=b'Photo creation date'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='photo',
            name='last_update_date',
            field=models.DateTimeField(auto_now=True, verbose_name=b'Photo last update date'),
            preserve_default=True,
        ),
    ]
