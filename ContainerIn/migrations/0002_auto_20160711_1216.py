# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ContainerIn', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='containerin',
            name='DISCHARGE_DATE',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='containerin',
            name='RAIL_ROUND_OUT',
            field=models.DateTimeField(),
        ),
    ]
