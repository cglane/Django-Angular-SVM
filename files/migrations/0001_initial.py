# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='csvFile',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('isPrimary', models.BooleanField(default=False)),
                ('title', models.CharField(default=b'', max_length=100, blank=True)),
                ('album', models.CharField(default=b'Main', max_length=100, blank=True)),
                ('comment', models.TextField(default=b'', blank=True)),
                ('csvFile', models.FileField(upload_to=b'csvFiles/%Y_%m_%d/')),
            ],
            options={
                'ordering': ('created',),
            },
            bases=(models.Model,),
        ),
    ]
