# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_auto_20150205_1728'),
    ]

    operations = [
        migrations.AddField(
            model_name='appotagameuser',
            name='server',
            field=models.CharField(default=b'1', max_length=100),
            preserve_default=True,
        ),
    ]
