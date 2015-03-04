# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0002_auto_20150304_1341'),
    ]

    operations = [
        migrations.AddField(
            model_name='member',
            name='user_type',
            field=models.CharField(default=b'member', max_length=50, editable=False),
            preserve_default=True,
        ),
    ]
