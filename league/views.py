from django.views.generic import TemplateView
from django.shortcuts import render, get_object_or_404, redirect
from rest_framework import generics, status
from rest_framework.response import Response
from django.core.mail import send_mail
from django.conf import settings
from django.utils.crypto import get_random_string
from .models import League, Invitation
from .serializers import LeagueSerializer, PlayerInvitationSerializer

from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.permissions import IsAuthenticated


class LeagueListCreate(generics.ListCreateAPIView):
    queryset = League.objects.all()
    serializer_class = LeagueSerializer


class LeagueDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = League.objects.all()
    serializer_class = LeagueSerializer


class InvitationListCreate(generics.ListCreateAPIView):
    queryset = Invitation.objects.all()
    serializer_class = PlayerInvitationSerializer

    def perform_create(self, serializer):
        team = serializer.validated_data['team']
        email = serializer.validated_data['email']
        token = get_random_string(64)
        invitation = serializer.save(token=token)

        # Send the invitation email
        url = '{}://{}'.format(self.request.scheme, self.request.get_host())
        invitation_url = f"{url}/league/accept-invitation/{token}/"
        send_mail(
            'Invitation to join team',
            f'You have been invited to join the {team.name}. Click the link to join: {invitation_url}',
            settings.EMAIL_HOST_USER,
            [email],
            fail_silently=False,
        )

    def create(self, request, *args, **kwargs):
        response = super().create(request, *args, **kwargs)
        return Response({'message': 'Invitation sent successfully'}, status=status.HTTP_201_CREATED)


class InvitationConfirmation(TemplateView):
    template_name = 'league/confirmation_page.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        token = self.kwargs.get('token')
        invitation = get_object_or_404(Invitation, token=token)
        invitation.accept_invitation()
        team = invitation.team
        context['team'] = team
        context['league'] = invitation.league
        return context
