# Generated by Django 4.0.3 on 2022-03-30 17:29

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('team', '0033_auto_20220330_1723'),
    ]

    operations = [
        migrations.AlterField(
            model_name='match',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2022, 3, 30, 17, 29, 30, 775079)),
        ),
        migrations.AlterField(
            model_name='team',
            name='name',
            field=models.CharField(default='<function uuid1 at 0x7f2c6e989bd0>', max_length=100, unique=True),
        ),
        migrations.AlterField(
            model_name='tournament',
            name='name',
            field=models.CharField(default='<function uuid3 at 0x7f2c6e989c60>', max_length=100, unique=True),
        ),
    ]
