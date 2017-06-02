# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-13 17:30
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_requestinvite_user_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='create_applications',
            field=models.BooleanField(default=False, help_text='Check this to allow the account to register applications.'),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='organization_name',
            field=models.CharField(blank=True, default='', max_length=255),
        ),
    ]