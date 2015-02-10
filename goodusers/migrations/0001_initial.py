# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='GoodUser',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('user_name', models.CharField(unique=True, max_length=100)),
                ('email', models.EmailField(max_length=75, null=True)),
                ('twitter_handle', models.CharField(max_length=100, null=True, blank=True)),
                ('facebook_handle', models.CharField(max_length=100, null=True, blank=True)),
                ('eyeem_handle', models.CharField(max_length=100, null=True, blank=True)),
                ('instagram_user_name', models.CharField(unique=True, max_length=100)),
                ('full_name', models.CharField(max_length=100)),
                ('instagram_user_full_name', models.CharField(max_length=100)),
                ('number_of_followers', models.IntegerField(default=0, null=True)),
                ('number_of_followings', models.IntegerField(default=0, null=True)),
                ('number_of_media', models.IntegerField(default=0, null=True)),
                ('creation_date', models.DateTimeField(auto_now_add=True, verbose_name=b'GoodUser creation date')),
                ('last_update_date', models.DateTimeField(auto_now=True, verbose_name=b'GoodUser creation date')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='GoodUsersCategories',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('good_user_id', models.IntegerField()),
                ('category_id', models.IntegerField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
