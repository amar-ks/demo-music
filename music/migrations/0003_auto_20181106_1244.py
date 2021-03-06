# Generated by Django 2.1.1 on 2018-11-06 07:14

import datetime
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('music', '0002_auto_20181103_2141'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='ProductionProfile',
            new_name='Profile',
        ),
        migrations.AlterField(
            model_name='album',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2018, 11, 6, 12, 44, 14, 191066)),
        ),
        migrations.AlterField(
            model_name='song',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2018, 11, 6, 12, 44, 14, 191880)),
        ),
    ]
