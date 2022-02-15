from django.db import models
from django.db.models import ForeignKey

# Create your models here.
class Team(models.Model):
    team_id = models.IntegerField(db_column='Team_ID', primary_key=True)  # Field name made lowercase.
    team_n = models.CharField(db_column='Team_N', max_length=20)  # Field name made lowercase.
    leagueid = models.IntegerField(db_column='LeagueID')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'team'

class League(models.Model):
    leagueid = models.IntegerField(db_column='LeagueID', primary_key=True)  # Field name made lowercase.
    leaguename = models.CharField(db_column='LeagueName', max_length=4)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'league'

class Teamstats2021P(models.Model):
    id = models.BigIntegerField(db_column='index', blank=True, primary_key=True)
    tid = models.ForeignKey(Team, to_field='team_id', related_name='teamstats', db_column='tID',
                                        on_delete=models.CASCADE)  # Field name made lowercase.
    tname = models.TextField(db_column='tName', blank=True, null=True)  # Field name made lowercase.
    stype = models.TextField(db_column='Stype', blank=True, null=True)  # Field name made lowercase.
    per = models.FloatField(blank=True, null=True)
    bc = models.FloatField(db_column='BC', blank=True, null=True)  # Field name made lowercase.
    o = models.FloatField(db_column='O', blank=True, null=True)  # Field name made lowercase.
    hit = models.BigIntegerField(blank=True, null=True)
    single = models.BigIntegerField(blank=True, null=True)
    double = models.BigIntegerField(blank=True, null=True)
    triple = models.BigIntegerField(blank=True, null=True)
    homerun = models.BigIntegerField(blank=True, null=True)
    tb = models.BigIntegerField(db_column='TB', blank=True, null=True)  # Field name made lowercase.
    r = models.FloatField(db_column='R', blank=True, null=True)  # Field name made lowercase.
    k = models.BigIntegerField(db_column='K', blank=True, null=True)  # Field name made lowercase.
    bb = models.FloatField(db_column='BB', blank=True, null=True)  # Field name made lowercase.
    db = models.FloatField(db_column='DB', blank=True, null=True)  # Field name made lowercase.
    dp = models.FloatField(db_column='DP', blank=True, null=True)  # Field name made lowercase.
    oba = models.FloatField(db_column='OBA', blank=True, null=True)  # Field name made lowercase.
    whip = models.FloatField(db_column='WHIP', blank=True, null=True)  # Field name made lowercase.
    era = models.FloatField(db_column='ERA', blank=True, null=True)  # Field name made lowercase.
    sw = models.FloatField(db_column='Sw', blank=True, null=True)  # Field name made lowercase.
    co = models.FloatField(db_column='Co', blank=True, null=True)  # Field name made lowercase.
    ssw = models.FloatField(db_column='SSw', blank=True, null=True)  # Field name made lowercase.
    sco = models.FloatField(db_column='SCo', blank=True, null=True)  # Field name made lowercase.
    bsw = models.FloatField(db_column='BSw', blank=True, null=True)  # Field name made lowercase.
    bco = models.FloatField(db_column='BCo', blank=True, null=True)  # Field name made lowercase.
    go = models.BigIntegerField(db_column='GO', blank=True, null=True)  # Field name made lowercase.
    fo = models.BigIntegerField(db_column='FO', blank=True, null=True)  # Field name made lowercase.
    ro = models.BigIntegerField(db_column='RO', blank=True, null=True)  # Field name made lowercase.
    pitcount = models.BigIntegerField(blank=True, null=True)
    pperpa = models.FloatField(db_column='PperPA', blank=True, null=True)  # Field name made lowercase.
    sitnum = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'teamstats2021p'
