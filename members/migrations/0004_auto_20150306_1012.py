# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0003_member_user_type'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='member',
            options={'ordering': ('user_id__username',), 'get_latest_by': 'creation_date', 'verbose_name': 'Member', 'verbose_name_plural': 'Members'},
        ),
    ]
