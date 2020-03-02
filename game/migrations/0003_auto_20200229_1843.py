# Generated by Django 3.0.2 on 2020-02-29 17:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0002_auto_20200229_1842'),
    ]

    operations = [
        migrations.CreateModel(
            name='Player',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField()),
                ('nationality', models.TextField()),
                ('rank', models.IntegerField()),
                ('atp_points', models.IntegerField()),
            ],
        ),
        migrations.AddField(
            model_name='team',
            name='player1',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='player1_player', to='game.Player'),
        ),
        migrations.AddField(
            model_name='team',
            name='player10',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='player10_player', to='game.Player'),
        ),
        migrations.AddField(
            model_name='team',
            name='player2',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='player2_player', to='game.Player'),
        ),
        migrations.AddField(
            model_name='team',
            name='player3',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='player3_player', to='game.Player'),
        ),
        migrations.AddField(
            model_name='team',
            name='player4',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='player4_player', to='game.Player'),
        ),
        migrations.AddField(
            model_name='team',
            name='player5',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='player5_player', to='game.Player'),
        ),
        migrations.AddField(
            model_name='team',
            name='player6',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='player6_player', to='game.Player'),
        ),
        migrations.AddField(
            model_name='team',
            name='player7',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='player7_player', to='game.Player'),
        ),
        migrations.AddField(
            model_name='team',
            name='player8',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='player8_player', to='game.Player'),
        ),
        migrations.AddField(
            model_name='team',
            name='player9',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='player9_player', to='game.Player'),
        ),
    ]
