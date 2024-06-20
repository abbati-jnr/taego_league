from rest_framework import serializers
from .models import Team, Invitation


class TeamSerializer(serializers.ModelSerializer):
    class Meta:
        model = Team
        fields = ['id', 'name', 'logo', 'league', 'description', 'team_manager', 'players']


class InvitationSerializer(serializers.ModelSerializer):

    class Meta:
        model = Invitation
        fields = ['id', 'email', 'team', 'date', 'accepted', 'token']
        extra_kwargs = {'token': {'read_only': True}, 'accepted': {'read_only': True}}
