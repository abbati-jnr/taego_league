from rest_framework import serializers
from .models import League, Invitation


class LeagueSerializer(serializers.ModelSerializer):
    class Meta:
        model = League
        fields = ['id', 'name', 'logo', 'description', 'admin', 'teams']


class PlayerInvitationSerializer(serializers.ModelSerializer):

    class Meta:
        model = Invitation
        fields = ['id', 'league', 'team', 'date', 'accepted', 'token']
        extra_kwargs = {'token': {'read_only': True}, 'accepted': {'read_only': True}}
