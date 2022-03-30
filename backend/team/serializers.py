from rest_framework import serializers

from .models import Tournament, Team, Player, Match


class TournamentSerializer(serializers.ModelSerializer):
    name = serializers.CharField(max_length=100, required=True)
    def create(self, validated_data):
    # Once the request data has been validated, we can create a todo item instance in the database
        T = Tournament.objects.create(name=validated_data.get('name'))
        for team in Team.objects.all():
            if team.name != 'Uncapped':
                self.team_set.add(team)
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
    def create(self, validated_data):
        T = Team.objects.create(name=validated_data.get('name'))
        try:
            T.tournament = validated_data.get('tournament')
            if(not len(T)):
                T.tournament = 'Idle Teams'
        except:
            pass
        T.save()
        return T
    def update(self, instance, validated_data):
        try:
            X = validated_data.get('name')
            if(len(X)):
                instance.name = X
        except:
            pass
        try:
            N = validated_data.get('tournament')
            if(len(N)):
                instance.tournament = N
        except:
            N = instance.tournament
        instance.tournament = N
        instance.save()
        return instance

    class Meta:
        model = Team
        fields = [
            'id',
            'tournament',
            'name',
            'player_set',
        ]
class PlayerSerializer(serializers.ModelSerializer):
    name = serializers.CharField(max_length=100, required=True)
    def create(self, validated_data):
        T = Player.objects.create(name=validated_data.get('name'),age = validated_data.get('age'),role = validated_data.get('role'))
        if(str(validated_data.get('team')) != "None"):
            T.team = validated_data.get('team')
        else:
            T.team = 'Uncapped'
        if(str(validated_data.get('bat')) != "None"):
            T.bathandedness = str(validated_data.get('bat'))
        else:
            T.bathandedness = 'right'
        if(str(validated_data.get('ball')) != "None"):
            T.ballhandedness = validated_data.get('ball')
        else:
            T.ballhandedness = 'right'
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
            'role'
        )
class MatchSerializer(serializers.ModelSerializer):
    name = serializers.CharField(max_length=100, required=True)
    def update(self, instance):
        instance.generate()
        instance.save()
        return instance
    class Meta:
        model = Match
        fields = (
            'id',
            'winner',
            'tournament',
            'scoreline_set',
            'playing11_set'
        )
