# Generated by Django 4.0.3 on 2022-03-26 09:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('team', '0008_remove_player_handedness_match_winner_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='team',
            name='name',
            field=models.CharField(default='<function uuid1 at 0x7f70d3909bd0>', max_length=100, unique=True),
        ),
        migrations.AlterField(
            model_name='tournament',
            name='name',
            field=models.CharField(default='<function uuid3 at 0x7f70d3909c60>', max_length=100, unique=True),
        ),
        migrations.CreateModel(
            name='Score',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('match', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='team.match')),
                ('player', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='team.player')),
            ],
        ),
    ]
