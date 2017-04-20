# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('animals', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Puppy',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=25)),
                ('color', models.CharField(max_length=25)),
                ('age', models.PositiveIntegerField()),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
