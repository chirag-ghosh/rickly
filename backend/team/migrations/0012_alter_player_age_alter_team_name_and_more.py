# Generated by Django 4.0.3 on 2022-03-29 11:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('team', '0011_alter_team_name_alter_tournament_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='player',
            name='age',
            field=models.PositiveIntegerField(default=20),
        ),
        migrations.AlterField(
            model_name='team',
            name='name',
            field=models.CharField(default='<function uuid1 at 0x7f9593a75bd0>', max_length=100, unique=True),
        ),
        migrations.AlterField(
            model_name='tournament',
            name='name',
            field=models.CharField(default='<function uuid3 at 0x7f9593a75c60>', max_length=100, unique=True),
        ),
    ]
