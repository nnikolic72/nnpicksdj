# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('goodusers', '0010_auto_20150304_1129'),
    ]

    operations = [
        migrations.AddField(
            model_name='gooduser',
            name='user_type',
            field=models.CharField(default=b'gooduser', max_length=50, editable=False),
            preserve_default=True,
        ),
    ]
