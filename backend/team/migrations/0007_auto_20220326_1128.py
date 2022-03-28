# Generated by Django 4.0.3 on 2022-03-26 05:58

from django.db import migrations

def initialize(apps, schema_editor):
    Tournament = apps.get_model('team','Tournament')
    Player = apps.get_model('team','Player')
    Team = apps.get_model('team','Team')
    Player.objects.all().delete()
    Team.objects.all().delete()
    Tournament.objects.all().delete()
    t = Tournament(name='Idle Teams')
    t.save()
    t = Team(name='Uncapped')
    t.save()

class Migration(migrations.Migration):
    initial = True
    dependencies = [
        ('team', '0006_alter_player_team_alter_team_name_and_more'),
    ]

    operations = [
        migrations.RunPython(initialize),
    ]
