from rest_framework import serializers
import random
from .models import Scoreline, Tournament, Team, Player, Match


class TournamentSerializer(serializers.ModelSerializer):
    name = serializers.CharField(max_length=100, required=True)
    def create(self, validated_data):
    # Once the request data has been validated, we can create a todo item instance in the database
        T = Tournament.objects.create(name=validated_data.get('name'))
        for team in Team.objects.all():
            if team.name != 'Uncapped':
                T.team_set.add(team)
                team.save()
        return T
    def post(self, instance, data):
        I = data.get('Schedule')
        try:
            i = int(I)
        except:
            return instance
        if(i):
            instance.setschedule()
            instance.save()
        return instance
    def update(self, instance, validated_data):
        # Once the request data has been validated, we can update the todo item instance in the database
        instance.name = validated_data.get('name', instance.name)
        instance.save()
        return instance

    class Meta:
        model = Tournament
        fields = (
            'id',
            'name',
            'match_num',
            'scheduled',
            'completed',
            'team_set',
            'match_set',
        )
class TeamSerializer(serializers.ModelSerializer):
    name = serializers.CharField(max_length=100, required=True)
    captain_name = serializers.SerializerMethodField('capname')
    wicketkeeper_name = serializers.SerializerMethodField('wicname')
    def capname(self, instance):
        return instance.player_set.all()[instance.captain].name
    def wicname(self, instance):
        return instance.player_set.all()[instance.wicketkeeper].name
    def create(self, validated_data):
        T = Team.objects.create(name=validated_data.get('name'))
        if(str(validated_data.get('tournament')) != "None"):
            T.tournament = validated_data.get('tournament')
        else:
            T.tournament = 'Idle Teams'
        U = Team.objects.all().filter(name='Uncapped')
        if U.player_set.count < 11:
            return
        else:
            for i in range(11):
                U.player_set.all()[0].team = T
                U.player_set.all()[0].save()
        T.captain = random.randint(0,10)
        T.wicketkeeper = random.randint(0,10)
        T.save()
        return T
    def update(self, instance, validated_data):
        if(str(validated_data.get('name')) != "None"):
            instance.name = validated_data.get('name')
        else:
            pass
        instance.save()
        if(str(validated_data.get('tournament')) != "None"):
            instance.tournament = validated_data.get('tournament')
        else:
            pass
        instance.save()
        return instance

    class Meta:
        model = Team
        fields = [
            'id',
            'tournament',
            'name',
            'player_set',
            'captain_name',
            'wicketkeeper_name',
        ]
class PlayerSerializer(serializers.ModelSerializer):
    name = serializers.CharField(max_length=100, required=True)
    def create(self, validated_data):
        T = Player.objects.create(name=validated_data.get('name'),age = validated_data.get('age'),role = validated_data.get('role'))
        if(str(validated_data.get('team')) != "None"):
            T.team = validated_data.get('team')
        else:
            pass
        if(str(validated_data.get('bat')) != "None"):
            T.bathandedness = str(validated_data.get('bat'))
        else:
            pass
        if(str(validated_data.get('ball')) != "None"):
            T.ballhandedness = validated_data.get('ball')
        else:
            pass
        T.save()
        if(str(validated_data.get('specs')) != "None"):
            T.specifics = validated_data.get('specs')
        else:
            T.specifics = 'None'
        T.save()
        return T
    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.age = validated_data.get('age', instance.age)
        instance.team = validated_data.get('team', instance.team)
        instance.bathandedness = validated_data.get('bat', instance.bathandedness)
        instance.ballhandedness = validated_data.get('ball', instance.ballhandedness)
        instance.specifics = validated_data.get('specs', instance.soecifics)
        instance.role = validated_data.get('role', instance.role)
        instance.save()
        return instance
    class Meta:
        model = Player
        fields = (
            'id',
            'name',
            'age',
            'team',
            'bathandedness',
            'ballhandedness',
            'specifics',
            'role',
            '_1Ccount',
            '_5wcount',
            'runcount',
            'wickount',
            'catcount',
            '_50count',
        )
class MatchSerializer(serializers.ModelSerializer):
    team_names = serializers.SerializerMethodField('team_name')
    scoreline_set = serializers.SerializerMethodField('scorer')
    def team_name(self, instance):
        L = []
        for i in instance.playing11_set.all():
            L.append(i.team.name)
        return L
    def scorer(self, instance):
        L = []
        for i in instance.playing11_set.all():
            M = []
            for j in i.scoreline_set.all():
                S = []
                for k in j.playerinline_set.all():
                    S.append((k.player.name,k.role))
                M.append(S)
                M.append(j.run)
                M.append(j.ballfaced)
                M.append(j.out)
                M.append(j.outdesc)
            L.append(M)
        return L
    def update(self, instance):
        instance.generate()
        instance.save()
        return instance
    class Meta:
        model = Match
        fields = (
            'id',
            'date',
            'winner',
            'result',
            'tournament',
            'scoreline_set',
            'playing11_set',
            'team_names',
        )
class StatSerializer(serializers.ModelSerializer):
    class Meta:
        model = Player
        fields = (
            'id',
            'name',
            'age',
            'team',
            'bathandedness',
            'ballhandedness',
            'specifics',
            'role',
            '_1Ccount',
            '_5wcount',
            'runcount',
            'wickount',
            'catcount',
            '_50count',
        )
