# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0008_auto_20171219_0026'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='avg_interest',
            field=models.FloatField(null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='item',
            name='avg_rating',
            field=models.FloatField(null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='user_item',
            name='item',
            field=models.ForeignKey(related_name='user_items', to='users.Item'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='user_item',
            name='user',
            field=models.ForeignKey(related_name='user_items', to=settings.AUTH_USER_MODEL),
            preserve_default=True,
        ),
    ]
