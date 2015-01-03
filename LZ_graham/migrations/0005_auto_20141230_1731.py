# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('LZ_graham', '0004_auto_20141229_1901'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='client',
            name='use_confirmaton',
        ),
        migrations.AddField(
            model_name='client',
            name='use_email_confirmaton',
            field=models.BooleanField(default=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='client',
            name='APN_name',
            field=models.CharField(default=b'FR', max_length=20, choices=[(b'FR', b'Free Mobile'), (b'SO', b'Orange'), (b'JR', b'SFR'), (b'SR', b'Bouygue Telecom')]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='client',
            name='receivers_email',
            field=models.EmailField(max_length=100),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='client',
            name='unlock_PIN_code',
            field=models.PositiveSmallIntegerField(),
            preserve_default=True,
        ),
    ]
