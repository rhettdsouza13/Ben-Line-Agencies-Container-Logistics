# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ContainerIn', '0005_auto_20160711_1243'),
    ]

    operations = [
        migrations.AlterField(
            model_name='containerin',
            name='ACCOUNT',
            field=models.CharField(max_length=200, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='containerin',
            name='DISCHARGE_DATE',
            field=models.CharField(max_length=50, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='containerin',
            name='POD',
            field=models.CharField(max_length=200, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='containerin',
            name='SIZE',
            field=models.CharField(max_length=50, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='containerin',
            name='STATUS',
            field=models.CharField(max_length=100, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='containerin',
            name='TERMINAL',
            field=models.CharField(max_length=200, null=True, blank=True),
        ),
    ]
