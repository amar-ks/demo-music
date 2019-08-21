# Generated by Django 2.1.1 on 2018-11-03 16:11

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('music', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProductionProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bio', models.TextField(blank=True, max_length=500)),
                ('location', models.CharField(blank=True, max_length=250)),
                ('birth_date', models.DateField(blank=True, null=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.RemoveField(
            model_name='album',
            name='is_created',
        ),
        migrations.AddField(
            model_name='album',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2018, 11, 3, 21, 41, 32, 197366)),
        ),
        migrations.AddField(
            model_name='song',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2018, 11, 3, 21, 41, 32, 198170)),
        ),
    ]
