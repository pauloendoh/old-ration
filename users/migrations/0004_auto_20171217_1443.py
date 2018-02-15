# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_auto_20171217_1436'),
    ]

    operations = [
        migrations.RenameField(
            model_name='item',
            old_name='created_b',
            new_name='created_by',
        ),
    ]
