# Generated by Django 3.2.5 on 2021-12-15 14:03

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('player2021', '0002_delete_boardmodel'),
    ]

    operations = [
        migrations.CreateModel(
            name='Player',
            fields=[
                ('playerid', models.BigIntegerField(db_column='playerID', primary_key=True, serialize=False)),
                ('name_main', models.TextField(blank=True, db_column='Name_main', null=True)),
                ('name_kana', models.TextField(blank=True, db_column='Name_kana', null=True)),
                ('team_n', models.TextField(blank=True, db_column='Team_N', null=True)),
                ('team_id', models.BigIntegerField(blank=True, db_column='Team_ID', null=True)),
                ('uni_num', models.BigIntegerField(blank=True, null=True)),
                ('posi', models.TextField(blank=True, null=True)),
                ('birthday', models.TextField(blank=True, db_column='Birthday', null=True)),
                ('birthplace', models.TextField(blank=True, db_column='Birthplace', null=True)),
                ('tall', models.TextField(blank=True, db_column='Tall', null=True)),
                ('weight', models.TextField(blank=True, db_column='Weight', null=True)),
                ('bloodtype', models.TextField(blank=True, db_column='Bloodtype', null=True)),
                ('pit_bat', models.TextField(blank=True, db_column='Pit_Bat', null=True)),
                ('draft', models.TextField(blank=True, null=True)),
                ('year', models.TextField(blank=True, null=True)),
                ('old_school', models.TextField(blank=True, null=True)),
                ('title', models.TextField(blank=True, db_column='Title', null=True)),
                ('summary', models.TextField(blank=True, null=True)),
            ],
            options={
                'db_table': 'player',
                'managed': False,
            },
        ),
    ]
