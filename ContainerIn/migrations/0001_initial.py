# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ContainerIn',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('VSL_NAME', models.CharField(max_length=200)),
                ('VOY_NUMBER', models.CharField(max_length=200)),
                ('CONTAINER_NO', models.CharField(max_length=200)),
                ('TERMINAL', models.CharField(max_length=200)),
                ('ACCOUNT', models.CharField(max_length=200)),
                ('SIZE', models.CharField(max_length=50)),
                ('STATUS', models.CharField(max_length=100)),
                ('POD', models.CharField(max_length=200)),
                ('DISCHARGE_DATE', models.DateTimeField(default=1)),
                ('RAIL_ROUND_OUT', models.DateTimeField(default=1)),
                ('EMPTY_IN', models.CharField(max_length=200)),
                ('YARD', models.CharField(max_length=200)),
                ('REMARKS', models.CharField(max_length=2000)),
            ],
        ),
    ]
