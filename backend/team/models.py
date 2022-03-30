from django.db import models
import uuid
import random
from datetime import datetime, timedelta
import math
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
            list_of_matches = []
            for a in self.team_set.all():
                for b in self.team_set.all():
                    if(a.id < b.id):
                        list_of_matches.append((a,b))
            random.shuffle(list_of_matches)
            self.match_num = len(list_of_matches)
            timeofmatch = datetime.now()
            for F in list_of_matches:
                self.match_set.create(date = timeofmatch)
                M = self.match_set.get(date = timeofmatch)
                M.playing11_set.create(team = F[0],num=0)
                M.playing11_set.create(team = F[1],num=1)
                timeofmatch = timeofmatch + timedelta(days = 1)
            self.scheduled = True
        return

class Team(models.Model):
    name = models.CharField(max_length=100,unique=True,default=str(uuid.uuid1))
    tournament = models.ForeignKey(Tournament, default = 'Idle Teams', to_field='name', on_delete = models.SET_DEFAULT, null=True)
    win = models.PositiveBigIntegerField(default=0)
    loss = models.PositiveBigIntegerField(default=0)
    DNR = models.PositiveBigIntegerField(default=0)
    Point = models.PositiveBigIntegerField(default=0)
    def __str__(self):
        return self.name

class Match(models.Model):
    tournament = models.ForeignKey(Tournament,on_delete=models.CASCADE)
    result = models.BooleanField(default=1)
    winner = models.BooleanField(default=0)
    date = models.DateTimeField(default=datetime.now())
    def generate(self):
        batf = random.randint(0,1)
        lcount = random.randint(2,11)
        bt = self.playing11_set.get(num=batf)
        wt = self.playing11_set.get(num=1-batf)
        nbcount = random.randint(0,5)
        ao = 0
        if(lcount == 11): 
            ao = random.randint(0,1)
        ballremaining = 120 + nbcount
        nocount = 1 - ao
        frun = 0
        extra = nbcount + random(0,15)
        frun += extra
        for i in range(1,lcount+1):
            L = bt.scoreline_set.create(ballfaced = random.randint(1,ballremaining - lcount + i),ln=i)
            if(not ao and i == lcount):
                L.ballfaced = ballremaining            
            ballremaining -= L.ballfaced
            L.run = random.randint(0,6*L.ballfaced)
            frun += L.run
            batter = L.playerInLine_set.create(player = bt.team.player_set.all()[i-1],role='batter')
            batter.player.runcount += L.run
            x = random.randint(i,lcount)
            if((x == i and nocount == 1) or (i == lcount and not ao)):   #not out
                L.outdesc = 'Not'
                nocount = 0
            else:   #how wicket fell
                x = random.randint(0,980)
                if(x < 214):
                    L.outdesc = 'Bowled'
                    bowler = L.playerInLine_set.create(player = wt.team.player_set.all()[random.randint(6,10)],role='bowler')
                    bowler.player.wickount += 1
                elif(x < 783):
                    L.outdesc = 'Caught'
                    bowler = L.playerInLine_set.create(player = wt.team.player_set.all()[random.randint(6,10)],role='bowler')
                    bowler.player.wickount += 1
                    fielder = L.playerInLine_set.create(player = wt.team.player_set.all()[random.randint(0,10)])
                    fielder.player.catcount += 1
                elif(x < 926):
                    L.outdesc = 'LBW'
                    bowler = L.playerInLine_set.create(player = wt.team.player_set.all()[random.randint(6,10)],role='bowler')
                    bowler.player.wickount += 1
                elif(x < 960):
                    L.outdesc = 'Run'
                    fielder = L.playerInLine_set.create(player = wt.team.player_set.all()[random.randint(0,10)])
                else:
                    L.outdesc = 'Caught'
                    bowler = L.playerInLine_set.create(player = wt.team.player_set.all()[random.randint(6,10)],role='bowler')
                    bowler.player.wickount += 1
                    x = list(wt.team.player_set.all().filter(role='wicketkeeper'))
                    if(not len(x)):
                        fielder = L.playerInLine_set.create(player = wt.team.player_set.all()[random.randint(0,10)])
                    else:
                        fielder = L.playerInLine_set.create(player = x[random.randint(0,len(x)-1)])
        win = random.randint(0,44)
        if(win < 22):
            result = True
            win = False
            chasrun = random.randint(0,frun-1)
            runremaining = chasrun
            nbcount = random.randint(0,5)
            extra = nbcount + random.randint(0,15)
            runremaining -= extra
            ballremaining = 120 + nbcount
            ao = 0
            if(lcount == 11): 
                ao = random.randint(0,1)
            nocount = 1 - ao
            for i in range(1,lcount+1):
                L = wt.scoreline_set.create(run = random.randint(0,runremaining),ln=i)
                if(lcount != 11 and i == lcount):
                    L.run = runremaining
                runremaining -= L.run
                L.ballfaced = random.randint(math.ceil(L.run/6),ballremaining - lcount + i)
                ballremaining -= L.ballfaced
                batter = L.playerInLine_set.create(player = wt.team.player_set.all()[i-1],role='batter')
                batter.player.runcount += L.run
                x = random.randint(i,lcount)
                if((x == i and nocount == 1) or i == lcount):   #not out
                    L.outdesc = 'Not'
                    nocount = 0
                else:   #how wicket fell
                    x = random.randint(0,980)
                    if(x < 214):
                        L.outdesc = 'Bowled'
                        bowler = L.playerInLine_set.create(player = bt.team.player_set.all()[random.randint(6,10)],role='bowler')
                        bowler.player.wickount += 1
                    elif(x < 783):
                        L.outdesc = 'Caught'
                        bowler = L.playerInLine_set.create(player = bt.team.player_set.all()[random.randint(6,10)],role='bowler')
                        bowler.player.wickount += 1
                        fielder = L.playerInLine_set.create(player = bt.team.player_set.all()[random.randint(0,10)])
                        fielder.player.catcount += 1
                    elif(x < 926):
                        L.outdesc = 'LBW'
                        bowler = L.playerInLine_set.create(player = bt.team.player_set.all()[random.randint(6,10)],role='bowler')
                        bowler.player.wickount += 1
                    elif(x < 960):
                        L.outdesc = 'Run'
                        fielder = L.playerInLine_set.create(player = bt.team.player_set.all()[random.randint(0,10)])
                    else:
                        L.outdesc = 'Caught'
                        bowler = L.playerInLine_set.create(player = bt.team.player_set.all()[random.randint(6,10)],role='bowler')
                        bowler.player.wickount += 1
                        x = list(bt.team.player_set.all().filter(role='wicketkeeper'))
                        if(not len(x)):
                            fielder = L.playerInLine_set.create(player = bt.team.player_set.all()[random.randint(0,10)])
                        else:
                            fielder = L.playerInLine_set.create(player = x[random.randint(0,len(x)-1)])
        elif(win < 22):
            result = True
            win = False
            chasrun = random.randint(0,frun-1)
            runremaining = chasrun
            nbcount = random.randint(0,5)
            extra = nbcount + random.randint(0,15)
            runremaining -= extra
            ballremaining = 120 + nbcount
            ao = 0
            if(lcount == 11): 
                ao = random.randint(0,1)
            nocount = 1 - ao
            for i in range(1,lcount+1):
                L = wt.scoreline_set.create(run = random.randint(0,runremaining),ln=i)
                if(lcount != 11 and i == lcount):
                    L.run = runremaining
                runremaining -= L.run
                L.ballfaced = random.randint(math.ceil(L.run/6),ballremaining - lcount + i)
                ballremaining -= L.ballfaced
                batter = L.playerInLine_set.create(player = wt.team.player_set.all()[i-1],role='batter')
                batter.player.runcount += L.run
                x = random.randint(i,lcount)
                if((x == i and nocount == 1) or i == lcount):   #not out
                    L.outdesc = 'Not'
                    nocount = 0
                else:   #how wicket fell
                    x = random.randint(0,980)
                    if(x < 214):
                        L.outdesc = 'Bowled'
                        bowler = L.playerInLine_set.create(player = bt.team.player_set.all()[random.randint(6,10)],role='bowler')
                        bowler.player.wickount += 1
                    elif(x < 783):
                        L.outdesc = 'Caught'
                        bowler = L.playerInLine_set.create(player = bt.team.player_set.all()[random.randint(6,10)],role='bowler')
                        bowler.player.wickount += 1
                        fielder = L.playerInLine_set.create(player = bt.team.player_set.all()[random.randint(0,10)])
                        fielder.player.catcount += 1
                    elif(x < 926):
                        L.outdesc = 'LBW'
                        bowler = L.playerInLine_set.create(player = bt.team.player_set.all()[random.randint(6,10)],role='bowler')
                        bowler.player.wickount += 1
                    elif(x < 960):
                        L.outdesc = 'Run'
                        fielder = L.playerInLine_set.create(player = bt.team.player_set.all()[random.randint(0,10)])
                    else:
                        L.outdesc = 'Caught'
                        bowler = L.playerInLine_set.create(player = bt.team.player_set.all()[random.randint(6,10)],role='bowler')
                        bowler.player.wickount += 1
                        x = list(bt.team.player_set.all().filter(role='wicketkeeper'))
                        if(not len(x)):
                            fielder = L.playerInLine_set.create(player = bt.team.player_set.all()[random.randint(0,10)])
                        else:
                            fielder = L.playerInLine_set.create(player = x[random.randint(0,len(x)-1)])
            
class Playing11(models.Model):
    team = models.ForeignKey(Team, on_delete=models.CASCADE)
    match = models.ForeignKey(Match, on_delete=models.CASCADE)
    num = models.PositiveSmallIntegerField(default=0)

class Player(models.Model):
    name = models.CharField(max_length=100)
    role = models.CharField(max_length=20,default='wicketkeeper')
    bathandedness = models.CharField(max_length=10,null=True)
    ballhandedness = models.CharField(max_length=10,null=True)
    age = models.PositiveIntegerField(default=20)
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

class Scoreline(models.Model):
    run = models.PositiveIntegerField(default=0)
    ballfaced = models.PositiveIntegerField(default=0)
    out = models.BooleanField(default=False)
    outdesc = models.CharField(default='Not',max_length=100)
    play = models.ForeignKey(Playing11,on_delete=models.CASCADE)
    ln = models.PositiveSmallIntegerField(default=1)


class PlayerInLine(models.Model):
    player = models.ForeignKey(Player, on_delete=models.CASCADE)
    score = models.ForeignKey(Scoreline, on_delete=models.CASCADE)
    role = models.CharField(max_length=100, default='fielder')
