# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_auto_20171217_1102'),
    ]

    operations = [
        migrations.RenameField(
            model_name='item',
            old_name='created_by',
            new_name='created_b',
        ),
    ]
