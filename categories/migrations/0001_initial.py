# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(default=b'', max_length=200)),
                ('description', models.CharField(default=b'', max_length=200, null=True, blank=True)),
                ('slug', models.CharField(default=b'', max_length=50, null=True, blank=True)),
                ('app', models.CharField(default=b'', max_length=20, null=True, blank=True)),
                ('parent', models.ForeignKey(to='categories.Category')),
            ],
            options={
                'ordering': ('app', 'title'),
                'verbose_name': 'Category',
                'verbose_name_plural': 'Categories',
            },
            bases=(models.Model,),
        ),
    ]
