# Generated by Django 4.0.3 on 2022-03-30 05:09

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('team', '0023_alter_match_date_alter_team_name_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='team',
            name='Point',
        ),
        migrations.AlterField(
            model_name='match',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2022, 3, 30, 10, 39, 0, 975036)),
        ),
        migrations.AlterField(
            model_name='player',
            name='ballhandedness',
            field=models.CharField(default='right', max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='player',
            name='bathandedness',
            field=models.CharField(default='right', max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='team',
            name='name',
            field=models.CharField(default='<function uuid1 at 0x7ff9e3e89bd0>', max_length=100, unique=True),
        ),
        migrations.AlterField(
            model_name='tournament',
            name='name',
            field=models.CharField(default='<function uuid3 at 0x7ff9e3e89c60>', max_length=100, unique=True),
        ),
    ]
