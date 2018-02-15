# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0007_auto_20171218_1751'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user_item',
            name='item',
            field=models.ForeignKey(related_name='user_item', to='users.Item'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='user_item',
            name='user',
            field=models.ForeignKey(related_name='user_item', to=settings.AUTH_USER_MODEL),
            preserve_default=True,
        ),
    ]
