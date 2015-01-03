# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('LZ_graham', '0005_auto_20141230_1731'),
    ]

    operations = [
        migrations.AlterField(
            model_name='client',
            name='APN_name',
            field=models.CharField(default=b'free', max_length=20, choices=[(b'free', b'Free Mobile'), (b'orange', b'Orange'), (b'sfr', b'SFR'), (b'bouygue', b'Bouygue Telecom')]),
            preserve_default=True,
        ),
    ]
