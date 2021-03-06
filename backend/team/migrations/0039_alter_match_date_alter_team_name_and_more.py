# Generated by Django 4.0.3 on 2022-03-31 08:13

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('team', '0038_auto_20220331_0007'),
    ]

    operations = [
        migrations.AlterField(
            model_name='match',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2022, 3, 31, 8, 13, 38, 625217)),
        ),
        migrations.AlterField(
            model_name='team',
            name='name',
            field=models.CharField(default='Justine Keane', max_length=100, unique=True),
        ),
        migrations.AlterField(
            model_name='tournament',
            name='name',
            field=models.CharField(default='Karen Clifton', max_length=100, unique=True),
        ),
    ]
