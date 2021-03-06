# Generated by Django 4.0.3 on 2022-03-26 05:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('team', '0005_alter_team_name_alter_team_tournament_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='player',
            name='team',
            field=models.ForeignKey(default='Uncapped', null=True, on_delete=django.db.models.deletion.SET_DEFAULT, to='team.team', to_field='name'),
        ),
        migrations.AlterField(
            model_name='team',
            name='name',
            field=models.CharField(default='<function uuid1 at 0x7f69d6c8dbd0>', max_length=100, unique=True),
        ),
        migrations.AlterField(
            model_name='tournament',
            name='name',
            field=models.CharField(default='<function uuid3 at 0x7f69d6c8dc60>', max_length=100, unique=True),
        ),
    ]
