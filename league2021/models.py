from django.db import models

class League(models.Model):
    leagueid = models.IntegerField(db_column='LeagueID', primary_key=True)  # Field name made lowercase.
    leaguename = models.CharField(db_column='LeagueName', max_length=4)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'league'

class Leaguestats2021(models.Model):
    index = models.BigIntegerField(blank=True, primary_key=True)
    lid = models.ForeignKey(League, to_field='leagueid', related_name='league', db_column='LID', on_delete=models.CASCADE)  # Field name made lowercase.
    lname = models.TextField(db_column='lName', blank=True, null=True)  # Field name made lowercase.
    stype = models.TextField(db_column='Stype', blank=True, null=True)  # Field name made lowercase.
    per = models.FloatField(blank=True, null=True)
    pa = models.FloatField(db_column='PA', blank=True, null=True)  # Field name made lowercase.
    ab = models.FloatField(db_column='AB', blank=True, null=True)  # Field name made lowercase.
    hit = models.BigIntegerField(blank=True, null=True)
    single = models.BigIntegerField(blank=True, null=True)
    double = models.BigIntegerField(blank=True, null=True)
    triple = models.BigIntegerField(blank=True, null=True)
    homerun = models.BigIntegerField(blank=True, null=True)
    tb = models.BigIntegerField(db_column='TB', blank=True, null=True)  # Field name made lowercase.
    rbi = models.FloatField(db_column='RBI', blank=True, null=True)  # Field name made lowercase.
    k = models.BigIntegerField(db_column='K', blank=True, null=True)  # Field name made lowercase.
    bb = models.FloatField(db_column='BB', blank=True, null=True)  # Field name made lowercase.
    db = models.FloatField(db_column='DB', blank=True, null=True)  # Field name made lowercase.
    sb = models.FloatField(db_column='SB', blank=True, null=True)  # Field name made lowercase.
    sf = models.FloatField(db_column='SF', blank=True, null=True)  # Field name made lowercase.
    dp = models.FloatField(db_column='DP', blank=True, null=True)  # Field name made lowercase.
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
        db_table = 'leaguestats2021'

class Statsrank2021(models.Model):
    index = models.BigIntegerField(blank=True, primary_key=True)
    pid = models.BigIntegerField(db_column='pID', blank=True, null=True)  # Field name made lowercase.
    tid = models.BigIntegerField(db_column='tID', blank=True, null=True)  # Field name made lowercase.
    lid = models.BigIntegerField(db_column='lID', blank=True, null=True)  # Field name made lowercase.
    name_main = models.TextField(db_column='Name_main', blank=True, null=True)  # Field name made lowercase.
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

    class Meta:
        managed = False
        db_table = 'statsrank2021'

class Statsrank2021P(models.Model):
    index = models.BigIntegerField(blank=True, primary_key=True)
    pid = models.BigIntegerField(db_column='pID', blank=True, null=True)  # Field name made lowercase.
    tid = models.BigIntegerField(db_column='tID', blank=True, null=True)  # Field name made lowercase.
    lid = models.BigIntegerField(db_column='lID', blank=True, null=True)  # Field name made lowercase.
    name_main = models.TextField(db_column='Name_main', blank=True, null=True)  # Field name made lowercase.
    bc = models.BigIntegerField(db_column='BC', blank=True, null=True)  # Field name made lowercase.
    o = models.BigIntegerField(db_column='O', blank=True, null=True)  # Field name made lowercase.
    hit = models.BigIntegerField(blank=True, null=True)
    single = models.BigIntegerField(blank=True, null=True)
    double = models.BigIntegerField(blank=True, null=True)
    triple = models.BigIntegerField(blank=True, null=True)
    homerun = models.BigIntegerField(blank=True, null=True)
    tb = models.BigIntegerField(db_column='TB', blank=True, null=True)  # Field name made lowercase.
    r = models.BigIntegerField(db_column='R', blank=True, null=True)  # Field name made lowercase.
    k = models.BigIntegerField(db_column='K', blank=True, null=True)  # Field name made lowercase.
    bb = models.BigIntegerField(db_column='BB', blank=True, null=True)  # Field name made lowercase.
    db = models.FloatField(db_column='DB', blank=True, null=True)  # Field name made lowercase.
    dp = models.BigIntegerField(db_column='DP', blank=True, null=True)  # Field name made lowercase.
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

    class Meta:
        managed = False
        db_table = 'statsrank2021p'


