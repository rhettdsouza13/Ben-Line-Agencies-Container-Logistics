# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ContainerIn', '0003_auto_20160711_1241'),
    ]

    operations = [
        migrations.AlterField(
            model_name='containerin',
            name='EMPTY_IN',
            field=models.CharField(max_length=200, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='containerin',
            name='REMARKS',
            field=models.CharField(max_length=2000, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='containerin',
            name='YARD',
            field=models.CharField(max_length=200, null=True, blank=True),
        ),
    ]
