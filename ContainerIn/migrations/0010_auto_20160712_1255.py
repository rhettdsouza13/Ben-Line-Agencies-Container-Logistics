# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ContainerIn', '0009_documents'),
    ]

    operations = [
        migrations.AlterField(
            model_name='documents',
            name='excel',
            field=models.FileField(upload_to=b'documents/%d'),
        ),
    ]
