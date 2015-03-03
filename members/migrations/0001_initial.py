# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('categories', '0005_categoryraw'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('goodusers', '0007_gooduser_times_processed_for_friends'),
        ('friends', '0002_friend_iconosquare_user_profile_page_url'),
        ('attributes', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Member',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('likes_in_last_hour', models.IntegerField(default=0, null=True, blank=True)),
                ('comments_in_last_hour', models.IntegerField(default=0, null=True, blank=True)),
                ('last_processed_date', models.DateTimeField(null=True, verbose_name=b'Dashboard user processed date', blank=True)),
                ('last_update_date', models.DateTimeField(auto_now=True, verbose_name=b'GoodUser creation date')),
                ('creation_date', models.DateTimeField(auto_now_add=True, verbose_name=b'GoodUser creation date')),
            ],
            options={
                'ordering': ('user_id__user_name',),
                'get_latest_by': 'creation_date',
                'verbose_name': 'Member',
                'verbose_name_plural': 'Members',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='MemberToFriend',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('follow_level', models.CharField(default=b'LOW', max_length=20, null=True, blank=True, choices=[(b'LOW', b'Low'), (b'HIGH', b'High'), (b'OFF', b'Off')])),
                ('rating', models.IntegerField(null=True, blank=True)),
                ('last_interacted_time', models.DateTimeField(null=True, blank=True)),
                ('interaction_result', models.BooleanField(default=False)),
                ('favorite', models.BooleanField(default=False)),
                ('friend', models.ForeignKey(to='friends.Friend')),
                ('member', models.ForeignKey(to='members.Member')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='MemberToGooduser',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('follow_level', models.CharField(default=b'LOW', max_length=20, null=True, blank=True, choices=[(b'LOW', b'Low'), (b'HIGH', b'High')])),
                ('rating', models.IntegerField(null=True, blank=True)),
                ('favorite', models.BooleanField(default=False)),
                ('gooduser', models.ForeignKey(to='goodusers.GoodUser')),
                ('member', models.ForeignKey(to='members.Member')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='member',
            name='goodusers_followings',
            field=models.ManyToManyField(to='goodusers.GoodUser', null=True, through='members.MemberToGooduser', blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='member',
            name='photo_attributes',
            field=models.ManyToManyField(to='attributes.Attribute', null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='member',
            name='photo_categories',
            field=models.ManyToManyField(to='categories.Category', null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='member',
            name='potential_friends',
            field=models.ManyToManyField(to='friends.Friend', null=True, through='members.MemberToFriend', blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='member',
            name='user_id',
            field=models.OneToOneField(to=settings.AUTH_USER_MODEL),
            preserve_default=True,
        ),
    ]
