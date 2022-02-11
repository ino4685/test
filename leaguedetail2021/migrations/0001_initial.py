# Generated by Django 3.2.5 on 2022-02-11 11:59

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
            name='Leaguestats2021',
            fields=[
                ('index', models.BigIntegerField(blank=True, primary_key=True, serialize=False)),
                ('lname', models.TextField(blank=True, db_column='lName', null=True)),
                ('stype', models.TextField(blank=True, db_column='Stype', null=True)),
                ('per', models.FloatField(blank=True, null=True)),
                ('pa', models.FloatField(blank=True, db_column='PA', null=True)),
                ('ab', models.FloatField(blank=True, db_column='AB', null=True)),
                ('hit', models.BigIntegerField(blank=True, null=True)),
                ('single', models.BigIntegerField(blank=True, null=True)),
                ('double', models.BigIntegerField(blank=True, null=True)),
                ('triple', models.BigIntegerField(blank=True, null=True)),
                ('homerun', models.BigIntegerField(blank=True, null=True)),
                ('tb', models.BigIntegerField(blank=True, db_column='TB', null=True)),
                ('rbi', models.FloatField(blank=True, db_column='RBI', null=True)),
                ('k', models.BigIntegerField(blank=True, db_column='K', null=True)),
                ('bb', models.FloatField(blank=True, db_column='BB', null=True)),
                ('db', models.FloatField(blank=True, db_column='DB', null=True)),
                ('sb', models.FloatField(blank=True, db_column='SB', null=True)),
                ('sf', models.FloatField(blank=True, db_column='SF', null=True)),
                ('dp', models.FloatField(blank=True, db_column='DP', null=True)),
                ('avg', models.FloatField(blank=True, db_column='AVG', null=True)),
                ('slg', models.FloatField(blank=True, db_column='SLG', null=True)),
                ('obp', models.FloatField(blank=True, db_column='OBP', null=True)),
                ('ops', models.FloatField(blank=True, db_column='OPS', null=True)),
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
                'db_table': 'leaguestats2021',
                'managed': False,
            },
        ),
    ]