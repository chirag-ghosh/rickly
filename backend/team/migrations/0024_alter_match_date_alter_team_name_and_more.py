# Generated by Django 4.0.3 on 2022-03-30 06:31

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('team', '0023_alter_match_date_alter_team_name_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='match',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2022, 3, 30, 12, 1, 19, 757162)),
        ),
        migrations.AlterField(
            model_name='team',
            name='name',
            field=models.CharField(default='<function uuid1 at 0x7f81a2aed120>', max_length=100, unique=True),
        ),
        migrations.AlterField(
            model_name='tournament',
            name='name',
            field=models.CharField(default='<function uuid3 at 0x7f81a2aed1b0>', max_length=100, unique=True),
        ),
    ]
