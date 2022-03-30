# Generated by Django 4.0.3 on 2022-03-29 14:44

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('team', '0018_alter_match_date_alter_team_name_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='match',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2022, 3, 29, 20, 14, 39, 822287)),
        ),
        migrations.AlterField(
            model_name='team',
            name='name',
            field=models.CharField(default='<function uuid1 at 0x7f2d12bc1bd0>', max_length=100, unique=True),
        ),
        migrations.AlterField(
            model_name='tournament',
            name='name',
            field=models.CharField(default='<function uuid3 at 0x7f2d12bc1c60>', max_length=100, unique=True),
        ),
    ]