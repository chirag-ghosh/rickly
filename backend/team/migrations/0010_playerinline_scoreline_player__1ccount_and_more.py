# Generated by Django 4.0.3 on 2022-03-26 10:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('team', '0009_alter_team_name_alter_tournament_name_score'),
    ]

    operations = [
        migrations.CreateModel(
            name='PlayerInLine',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Scoreline',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('run', models.PositiveIntegerField(default=0)),
                ('ballfaced', models.PositiveIntegerField(default=0)),
                ('out', models.BooleanField(default=False)),
                ('outdesc', models.CharField(default='Not', max_length=100)),
                ('play', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='team.playing11')),
            ],
        ),
        migrations.AddField(
            model_name='player',
            name='_1Ccount',
            field=models.PositiveBigIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='player',
            name='_50count',
            field=models.PositiveBigIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='player',
            name='_5wcount',
            field=models.PositiveBigIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='player',
            name='catcount',
            field=models.PositiveBigIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='player',
            name='runcount',
            field=models.PositiveBigIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='player',
            name='wickount',
            field=models.PositiveBigIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='team',
            name='name',
            field=models.CharField(default='<function uuid1 at 0x7f89f5bd9bd0>', max_length=100, unique=True),
        ),
        migrations.AlterField(
            model_name='tournament',
            name='name',
            field=models.CharField(default='<function uuid3 at 0x7f89f5bd9c60>', max_length=100, unique=True),
        ),
        migrations.DeleteModel(
            name='Score',
        ),
        migrations.AddField(
            model_name='playerinline',
            name='player',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='team.player'),
        ),
        migrations.AddField(
            model_name='playerinline',
            name='score',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='team.scoreline'),
        ),
    ]
