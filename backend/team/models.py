from django.db import models
import uuid
# Create your models here.
class Tournament(models.Model):
    name = models.CharField(max_length = 100,unique = True, default=str(uuid.uuid3))
    match_num = models.PositiveIntegerField(default=0)
    completed = models.BooleanField(default=False)
    scheduled = models.BooleanField(default=False)
    def __str__(self):
        return self.name
    def setschedule(self):
        if(not self.scheduled):
            print(self.team_set.count())

            self.scheduled = True
        return
class Team(models.Model):
    name = models.CharField(max_length=100,unique=True,default=str(uuid.uuid1))
    tournament = models.ForeignKey(Tournament, to_field = 'name', default = 'Idle Teams', on_delete = models.SET_DEFAULT, null=True)
    def __str__(self):
        return self.name
class Match(models.Model):
    tournament = models.ForeignKey(Tournament,on_delete=models.CASCADE)
    winner = models.BooleanField(default=0)
    date = models.DateTimeField('Time of Match')
class Playing11(models.Model):
    team = models.ForeignKey(Team, on_delete=models.CASCADE)
    match = models.ForeignKey(Match, on_delete=models.CASCADE)
class Player(models.Model):
    name = models.CharField(max_length=100)
    role = models.CharField(max_length=20)
    bathandedness = models.CharField(max_length=10,null=True)
    ballhandedness = models.CharField(max_length=10,null=True)
    age = models.IntegerField(default=20)
    runcount = models.PositiveBigIntegerField(default=0)
    wickount = models.PositiveBigIntegerField(default=0)
    catcount = models.PositiveBigIntegerField(default=0)
    _1Ccount = models.PositiveBigIntegerField(default=0)
    _5wcount = models.PositiveBigIntegerField(default=0)
    _50count = models.PositiveBigIntegerField(default=0)
    specifics = models.CharField(max_length=40,default="")
    team = models.ForeignKey(Team, default = 'Uncapped', to_field='name', on_delete=models.SET_DEFAULT, null=True) 
    def __str__(self):
        return self.name
    def EnterDetails(self):
        self.name = input()
        self.role = input()
        f = 0
        if(self.role.lower() == 'batter' or self.role.lower() ==  'wicketkeeper' or self.role.lower() == 'all-rounder'):
            self.bathandedness=input()
            f = 1
        if(self.role.lower() == 'bowler' or self.role.lower() == 'all-rounder'):
            self.ballhandedness=input()
            f = 1
        if(not f):
            raise ValueError("Wrong type of player selected")
        self.age=int(input())
        if(self.role.lower() == 'all-rounder' or self.role.lower() == 'bowler'):
            self.specifics=input()
        t = str(input())
        try:
            q = Team.objects.get(name=t)
            self.team = q
        except Exception as e:
            raise ValueError("No Team of This Name")
class Scoreline(models.Model):
    run = models.PositiveIntegerField(default=0)
    ballfaced = models.PositiveIntegerField(default=0)
    out = models.BooleanField(default=False)
    outdesc = models.CharField(default='Not',max_length=100)
    play = models.ForeignKey(Playing11,on_delete=models.CASCADE)
    def write(self):
        battername = input()
        try:
            batter = Player.objects.get(name=battername)
        except:
            raise ValueError("No Such Player")
        self.PlayerInLine_set.create(player=batter)
        wickettype = input()
        if(wickettype == 'bowled' or wickettype == 'caught' or wickettype == 'lbw' or wickettype == 'stumped'):
            bowlername = input()
            try:
                bowler = Player.objects.get(name=bowlername)
            except:
                raise ValueError("No Such Player")
            self.PlayerInLine_set.create(player=bowler)
        if(wickettype == 'caught' or wickettype == 'run' or wickettype == 'stumped'):
            fieldername = input()
            try:
                fielder = Player.objects.get(name=fieldername)
            except:
                raise ValueError("No Such Player")
            self.PlayerInLine_set.create(player=fielder)


class PlayerInLine(models.Model):
    player = models.ForeignKey(Player, on_delete=models.CASCADE)
    score = models.ForeignKey(Scoreline, on_delete=models.CASCADE)
