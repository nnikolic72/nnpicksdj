# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('categories', '0002_auto_20150226_1235'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'ordering': ('app', 'parent__title', 'title'), 'verbose_name': 'Category', 'verbose_name_plural': 'Categories'},
        ),
    ]
