# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AppotaGameUser',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('username', models.CharField(max_length=200)),
                ('coin', models.IntegerField(default=0)),
                ('gold', models.IntegerField(default=0)),
                ('ruby', models.IntegerField(default=0)),
                ('diamond', models.IntegerField(default=0)),
                ('vip', models.FloatField(default=0)),
                ('month_card', models.FloatField(default=0)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
