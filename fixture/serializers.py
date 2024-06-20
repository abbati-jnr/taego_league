from rest_framework import serializers
from .models import Fixture
from team.models import Team
from league.models import League


class FixtureSerializer(serializers.ModelSerializer):
    league_id = serializers.PrimaryKeyRelatedField(queryset=League.objects.all(), write_only=True, source='league')
    team1_id = serializers.PrimaryKeyRelatedField(queryset=Team.objects.all(), write_only=True, source='team1')
    team2_id = serializers.PrimaryKeyRelatedField(queryset=Team.objects.all(), write_only=True, source='team2')

    class Meta:
        model = Fixture
        depth = 1
        fields = ['id', 'league', 'team1', 'team2', 'date', 'time', 'location','league_id', 'team1_id', 'team2_id']
