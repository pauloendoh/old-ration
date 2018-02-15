# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_user_item'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user_item',
            name='interest',
            field=models.FloatField(blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='user_item',
            name='rating',
            field=models.FloatField(blank=True),
            preserve_default=True,
        ),
    ]
