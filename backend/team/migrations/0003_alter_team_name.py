# Generated by Django 4.0.3 on 2022-03-24 02:14

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('team', '0002_tournament_scheduled_alter_player_team_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='team',
            name='name',
            field=models.CharField(default=uuid.uuid1, max_length=100, unique=True),
        ),
    ]