# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ContainerIn', '0006_auto_20160712_1142'),
    ]

    operations = [
        migrations.AddField(
            model_name='containerin',
            name='ICD_LOCAL',
            field=models.CharField(default=1, max_length=50),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='containerin',
            name='STATUS',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
    ]
