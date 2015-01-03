# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('LZ_graham', '0003_auto_20141229_1857'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='client',
            name='client_text',
        ),
        migrations.AddField(
            model_name='client',
            name='client_name',
            field=models.CharField(default='???', max_length=40),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='client',
            name='APN_name',
            field=models.CharField(max_length=20),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='client',
            name='object_email',
            field=models.CharField(max_length=100),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='client',
            name='phone_number',
            field=models.CharField(max_length=12),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='client',
            name='receivers_email',
            field=models.CharField(max_length=100),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='client',
            name='receivers_phone',
            field=models.CharField(max_length=12),
            preserve_default=True,
        ),
    ]
