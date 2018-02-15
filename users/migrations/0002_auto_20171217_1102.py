# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='item',
            name='related',
        ),
        migrations.RemoveField(
            model_name='item',
            name='tags',
        ),
        migrations.DeleteModel(
            name='Tag',
        ),
        migrations.AddField(
            model_name='item',
            name='type',
            field=models.CharField(default=1, max_length=255),
            preserve_default=False,
        ),
    ]
