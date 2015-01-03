# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('LZ_graham', '0002_client_phone_number'),
    ]

    operations = [
        migrations.RenameField(
            model_name='client',
            old_name='APN_name_text',
            new_name='APN_name',
        ),
        migrations.RenameField(
            model_name='client',
            old_name='APN_password_text',
            new_name='APN_password',
        ),
        migrations.RenameField(
            model_name='client',
            old_name='APN_username_text',
            new_name='APN_username',
        ),
        migrations.RenameField(
            model_name='client',
            old_name='message_phone_text',
            new_name='message_phone',
        ),
        migrations.RenameField(
            model_name='client',
            old_name='object_email_text',
            new_name='object_email',
        ),
        migrations.RenameField(
            model_name='client',
            old_name='receivers_email_list',
            new_name='receivers_email',
        ),
        migrations.RenameField(
            model_name='client',
            old_name='receivers_phone_list',
            new_name='receivers_phone',
        ),
        migrations.RenameField(
            model_name='client',
            old_name='use_confirmaton_bool',
            new_name='use_confirmaton',
        ),
    ]
