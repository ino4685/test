# Generated by Django 3.2.5 on 2022-01-02 07:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('team2021', '0002_league'),
    ]

    operations = [
        migrations.CreateModel(
            name='Teamstats2021',
            fields=[
                ('id', models.BigIntegerField(blank=True, db_column='index', primary_key=True, serialize=False)),
                ('tname', models.TextField(blank=True, db_column='tName', null=True)),
                ('stype', models.TextField(blank=True, db_column='Stype', null=True)),
                ('per', models.FloatField(blank=True, null=True)),
                ('pa', models.BigIntegerField(blank=True, db_column='PA', null=True)),
                ('ab', models.BigIntegerField(blank=True, db_column='AB', null=True)),
                ('hit', models.BigIntegerField(blank=True, null=True)),
                ('single', models.BigIntegerField(blank=True, null=True)),
                ('double', models.BigIntegerField(blank=True, null=True)),
                ('triple', models.BigIntegerField(blank=True, null=True)),
                ('homerun', models.BigIntegerField(blank=True, null=True)),
                ('tb', models.BigIntegerField(blank=True, db_column='TB', null=True)),
                ('rbi', models.BigIntegerField(blank=True, db_column='RBI', null=True)),
                ('k', models.BigIntegerField(blank=True, db_column='K', null=True)),
                ('bb', models.BigIntegerField(blank=True, db_column='BB', null=True)),
                ('db', models.BigIntegerField(blank=True, db_column='DB', null=True)),
                ('sb', models.BigIntegerField(blank=True, db_column='SB', null=True)),
                ('sf', models.BigIntegerField(blank=True, db_column='SF', null=True)),
                ('dp', models.BigIntegerField(blank=True, db_column='DP', null=True)),
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
                'db_table': 'teamstats2021',
                'managed': False,
            },
        ),
    ]
