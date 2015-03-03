# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('attributes', '0001_initial'),
        ('goodusers', '0004_gooduserraw'),
    ]

    operations = [
        migrations.AddField(
            model_name='gooduser',
            name='user_attribute',
            field=models.ManyToManyField(to='attributes.Attribute', null=True, blank=True),
            preserve_default=True,
        ),
    ]
