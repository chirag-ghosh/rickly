from rest_framework import serializers

from .models import Tournament, Team, Player


class TournamentSerializer(serializers.ModelSerializer):
    name = serializers.CharField(max_length=100, required=True)

    def create(self, validated_data):
    # Once the request data has been validated, we can create a todo item instance in the database
        T = Tournament.objects.create(name=validated_data.get('name'))
        for team in Team.objects.get():
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
            T.Tournament = validated_data.get('Tournament')
        except:
            pass
        return T
    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.save()
        return instance
    class Meta:
        model = Team
        fields = (
            'name',
            'tournament'
        )