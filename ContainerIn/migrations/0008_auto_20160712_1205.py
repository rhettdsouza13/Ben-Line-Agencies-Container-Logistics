# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ContainerIn', '0007_auto_20160712_1155'),
    ]

    operations = [
        migrations.AlterField(
            model_name='containerin',
            name='STATUS',
            field=models.CharField(max_length=50),
        ),
    ]
