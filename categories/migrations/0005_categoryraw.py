# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('categories', '0004_auto_20150301_1009'),
    ]

    operations = [
        migrations.CreateModel(
            name='CategoryRaw',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(default=b'', max_length=200)),
                ('description', models.CharField(default=b'', max_length=200, null=True, blank=True)),
                ('parent', models.CharField(default=b'', max_length=200, null=True, blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
