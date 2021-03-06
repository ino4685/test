# Generated by Django 3.2.5 on 2022-02-17 12:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='League',
            fields=[
                ('leagueid', models.IntegerField(db_column='LeagueID', primary_key=True, serialize=False)),
                ('leaguename', models.CharField(db_column='LeagueName', max_length=4)),
            ],
            options={
                'db_table': 'league',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Team',
            fields=[
                ('team_id', models.IntegerField(db_column='Team_ID', primary_key=True, serialize=False)),
                ('team_n', models.CharField(db_column='Team_N', max_length=20)),
                ('leagueid', models.IntegerField(db_column='LeagueID')),
            ],
            options={
                'db_table': 'team',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Teamstats2021P',
            fields=[
                ('id', models.BigIntegerField(blank=True, db_column='index', primary_key=True, serialize=False)),
                ('tname', models.TextField(blank=True, db_column='tName', null=True)),
                ('stype', models.TextField(blank=True, db_column='Stype', null=True)),
                ('per', models.FloatField(blank=True, null=True)),
                ('bc', models.FloatField(blank=True, db_column='BC', null=True)),
                ('o', models.FloatField(blank=True, db_column='O', null=True)),
                ('hit', models.BigIntegerField(blank=True, null=True)),
                ('single', models.BigIntegerField(blank=True, null=True)),
                ('double', models.BigIntegerField(blank=True, null=True)),
                ('triple', models.BigIntegerField(blank=True, null=True)),
                ('homerun', models.BigIntegerField(blank=True, null=True)),
                ('tb', models.BigIntegerField(blank=True, db_column='TB', null=True)),
                ('r', models.FloatField(blank=True, db_column='R', null=True)),
                ('k', models.BigIntegerField(blank=True, db_column='K', null=True)),
                ('bb', models.FloatField(blank=True, db_column='BB', null=True)),
                ('db', models.FloatField(blank=True, db_column='DB', null=True)),
                ('dp', models.FloatField(blank=True, db_column='DP', null=True)),
                ('oba', models.FloatField(blank=True, db_column='OBA', null=True)),
                ('whip', models.FloatField(blank=True, db_column='WHIP', null=True)),
                ('era', models.FloatField(blank=True, db_column='ERA', null=True)),
                ('sw', models.FloatField(blank=True, db_column='Sw', null=True)),
                ('co', models.FloatField(blank=True, db_column='Co', null=True)),
                ('ssw', models.FloatField(blank=True, db_column='SSw', null=True)),
                ('sco', models.FloatField(blank=True, db_column='SCo', null=True)),
                ('bsw', models.FloatField(blank=True, db_column='BSw', null=True)),
                ('bco', models.FloatField(blank=True, db_column='BCo', null=True)),
                ('go', models.BigIntegerField(blank=True, db_column='GO', null=True)),
                ('fo', models.BigIntegerField(blank=True, db_column='FO', null=True)),
                ('ro', models.BigIntegerField(blank=True, db_column='RO', null=True)),
                ('pitcount', models.BigIntegerField(blank=True, null=True)),
                ('pperpa', models.FloatField(blank=True, db_column='PperPA', null=True)),
                ('sitnum', models.BigIntegerField(blank=True, null=True)),
            ],
            options={
                'db_table': 'teamstats2021p',
                'managed': False,
            },
        ),
    ]
