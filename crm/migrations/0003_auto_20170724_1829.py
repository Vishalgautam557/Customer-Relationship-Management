# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-07-25 01:29
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('crm', '0002_auto_20170724_1821'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Company_Agent_Relation',
            new_name='CompanyAgentRelation',
        ),
    ]
