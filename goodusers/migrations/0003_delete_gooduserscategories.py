# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('goodusers', '0002_gooduser_user_category'),
    ]

    operations = [
        migrations.DeleteModel(
            name='GoodUsersCategories',
        ),
    ]
