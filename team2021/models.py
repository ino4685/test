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

class Teamstats2021(models.Model):
    id = models.BigIntegerField(db_column='index', blank=True, primary_key=True)
    tid = models.ForeignKey(Team, to_field='team_id', related_name='teamstats', db_column='tID',
                                        on_delete=models.CASCADE)  # Field name made lowercase.
    tname = models.TextField(db_column='tName', blank=True, null=True)  # Field name made lowercase.
    stype = models.TextField(db_column='Stype', blank=True, null=True)  # Field name made lowercase.
    per = models.FloatField(blank=True, null=True)
    pa = models.BigIntegerField(db_column='PA', blank=True, null=True)  # Field name made lowercase.
    ab = models.BigIntegerField(db_column='AB', blank=True, null=True)  # Field name made lowercase.
    hit = models.BigIntegerField(blank=True, null=True)
    single = models.BigIntegerField(blank=True, null=True)
    double = models.BigIntegerField(blank=True, null=True)
    triple = models.BigIntegerField(blank=True, null=True)
    homerun = models.BigIntegerField(blank=True, null=True)
    tb = models.BigIntegerField(db_column='TB', blank=True, null=True)  # Field name made lowercase.
    rbi = models.BigIntegerField(db_column='RBI', blank=True, null=True)  # Field name made lowercase.
    k = models.BigIntegerField(db_column='K', blank=True, null=True)  # Field name made lowercase.
    bb = models.BigIntegerField(db_column='BB', blank=True, null=True)  # Field name made lowercase.
    db = models.BigIntegerField(db_column='DB', blank=True, null=True)  # Field name made lowercase.
    sb = models.BigIntegerField(db_column='SB', blank=True, null=True)  # Field name made lowercase.
    sf = models.BigIntegerField(db_column='SF', blank=True, null=True)  # Field name made lowercase.
    dp = models.BigIntegerField(db_column='DP', blank=True, null=True)  # Field name made lowercase.
    avg = models.FloatField(db_column='AVG', blank=True, null=True)  # Field name made lowercase.
    slg = models.FloatField(db_column='SLG', blank=True, null=True)  # Field name made lowercase.
    obp = models.FloatField(db_column='OBP', blank=True, null=True)  # Field name made lowercase.
    ops = models.FloatField(db_column='OPS', blank=True, null=True)  # Field name made lowercase.
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
        db_table = 'teamstats2021'

class Player(models.Model):
    playerid = models.BigIntegerField(db_column='playerID', primary_key=True)  # Field name made lowercase.
    name_main = models.TextField(db_column='Name_main', blank=True, null=True)  # Field name made lowercase.
    name_kana = models.TextField(db_column='Name_kana', blank=True, null=True)  # Field name made lowercase.
    team_n = models.TextField(db_column='Team_N', blank=True, null=True)  # Field name made lowercase.
    ptid = models.ForeignKey(Team, to_field='team_id', related_name='TeamPlayer', db_column='Team_ID',
                             on_delete=models.CASCADE) # Field name made lowercase.
    uni_num = models.TextField(blank=True, null=True)
    posi = models.TextField(blank=True, null=True)
    birthday = models.TextField(db_column='Birthday', blank=True, null=True)  # Field name made lowercase.
    birthplace = models.TextField(db_column='Birthplace', blank=True, null=True)  # Field name made lowercase.
    tall = models.TextField(db_column='Tall', blank=True, null=True)  # Field name made lowercase.
    weight = models.TextField(db_column='Weight', blank=True, null=True)  # Field name made lowercase.
    bloodtype = models.TextField(db_column='Bloodtype', blank=True, null=True)  # Field name made lowercase.
    pit_bat = models.TextField(db_column='Pit_Bat', blank=True, null=True)  # Field name made lowercase.
    draft = models.TextField(blank=True, null=True)
    year = models.TextField(blank=True, null=True)
    old_school = models.TextField(blank=True, null=True)
    title = models.TextField(db_column='Title', blank=True, null=True)  # Field name made lowercase.
    summary = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'player'