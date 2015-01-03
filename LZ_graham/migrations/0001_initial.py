# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('client_text', models.CharField(max_length=200)),
                ('creation_date', models.DateTimeField(verbose_name=b'date created')),
                ('unlock_PIN_code', models.IntegerField(default=1234)),
                ('APN_name_text', models.CharField(max_length=100)),
                ('APN_username_text', models.CharField(max_length=30)),
                ('APN_password_text', models.CharField(max_length=30)),
                ('message_phone_text', models.CharField(max_length=2000)),
                ('receivers_phone_list', models.CharField(max_length=200)),
                ('use_confirmaton_bool', models.IntegerField(default=1)),
                ('object_email_text', models.CharField(max_length=200)),
                ('receivers_email_list', models.CharField(max_length=200)),
            ],
            options=None,
            bases=None,
            managers=None,
        ),
    ]
