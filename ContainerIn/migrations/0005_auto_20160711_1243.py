# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ContainerIn', '0004_auto_20160711_1242'),
    ]

    operations = [
        migrations.AlterField(
            model_name='containerin',
            name='RAIL_ROUND_OUT',
            field=models.CharField(max_length=50, null=True, blank=True),
        ),
    ]
