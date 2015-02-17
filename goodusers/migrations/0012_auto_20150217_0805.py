# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('goodusers', '0011_auto_20150215_0742'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='gooduser',
            options={'ordering': ('user_name',), 'get_latest_by': 'creation_date', 'verbose_name': 'Good User', 'verbose_name_plural': 'Good Users'},
        ),
        migrations.AddField(
            model_name='gooduser',
            name='instagram_user_name_valid',
            field=models.BooleanField(default=True, help_text='Check if Instagram user is valid/exists.'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='gooduser',
            name='instagram_user_bio',
            field=models.TextField(max_length=500, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='gooduser',
            name='to_be_processed',
            field=models.BooleanField(default=True, help_text='Check if you want this Good User to be processed in the next Batch Run'),
            preserve_default=True,
        ),
    ]
