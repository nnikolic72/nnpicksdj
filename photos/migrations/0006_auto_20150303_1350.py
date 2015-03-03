# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('categories', '0004_auto_20150301_1009'),
        ('attributes', '0001_initial'),
        ('photos', '0005_auto_20150302_1523'),
    ]

    operations = [
        migrations.AddField(
            model_name='photo',
            name='photo_attribute',
            field=models.ManyToManyField(to='attributes.Attribute', null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='photo',
            name='photo_category',
            field=models.ManyToManyField(to='categories.Category', null=True, blank=True),
            preserve_default=True,
        ),
    ]
