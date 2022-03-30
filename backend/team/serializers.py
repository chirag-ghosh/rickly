from rest_framework import serializers

from .models import Tournament, Team, Player, Match


class TournamentSerializer(serializers.ModelSerializer):
    name = serializers.CharField(max_length=100, required=True)

    def create(self, validated_data):
    # Once the request data has been validated, we can create a todo item instance in the database
        T = Tournament.objects.create(name=validated_data.get('name'))
        for team in Team.objects.all():
            if team.name != 'Uncapped':
                team.Tournament = T
        return T
    def schedule(self, instance):
        instance.setschedule()
        return
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
        )
class TeamSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=100, required=True)
    def create(self, validated_data):
        T = Team.objects.create(name=validated_data.get('name'))
        try:
            T.tournament = validated_data.get('tournament')
        except:
            pass
        return T
    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.tournament = validated_data.get('tournament', instance.tournament)
        instance.save()
        return instance
    class Meta:
        model = Team
        fields = (
            'name',
            'tournament',
            'id',
        )
class PlayerSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=100, required=True)
    def create(self, validated_data):
        T = Player.objects.create(name=validated_data.get('name'))
        try:
            T.team = validated_data.get('team')
        except:
            pass
        T.age = validated_data.get('age')
        T.role = validated_data.get('role')
        try:
            T.bathandedness = validated_data.get('bat')
        except:
            pass
        try:
            T.ballhandedness = validated_data.get('ball')
        except:
            pass
        try:
            T.specifics = validated_data.get('specs')
        except:
            pass
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
            'name',
            'age',
            'team',
            'bathandedness',
            'ballhandedness',
            'specifics',
            'role'
        )
class MatchSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=100, required=True)
    def update(self, instance, validated_data):
        instance.generate()
        instance.save()
        return instance
    class Meta:
        model = Match
        fields = (
            'name',
            'tournament'
        )
