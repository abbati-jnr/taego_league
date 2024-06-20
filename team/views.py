from rest_framework import generics
from django.shortcuts import render, get_object_or_404
from rest_framework import generics, status
from rest_framework.response import Response
from django.views.generic import TemplateView
from .models import Team, Invitation
from .serializers import TeamSerializer, InvitationSerializer
from django.core.mail import send_mail
from django.conf import settings
from django.utils.crypto import get_random_string


class TeamListCreate(generics.ListCreateAPIView):
    queryset = Team.objects.all()
    serializer_class = TeamSerializer


class TeamDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Team.objects.all()
    serializer_class = TeamSerializer


class InvitationListCreate(generics.ListCreateAPIView):
    queryset = Invitation.objects.all()
    serializer_class = InvitationSerializer

    def perform_create(self, serializer):
        league = serializer.validated_data['league']
        team = serializer.validated_data['team']
        email = team.team_manager
        token = get_random_string(64)
        invitation = serializer.save(token=token)

        # Send the invitation email
        url = '{}://{}'.format(self.request.scheme, self.request.get_host())
        invitation_url = f"{url}/team/accept-invitation/{token}/"
        send_mail(
            'Invitation to join league',
            f'You have been invited to join the {league.name}. Click the link to join: {invitation_url}',
            settings.EMAIL_HOST_USER,
            [email],
            fail_silently=False,
        )

    def create(self, request, *args, **kwargs):
        response = super().create(request, *args, **kwargs)
        return Response({'message': 'Invitation sent successfully'}, status=status.HTTP_201_CREATED)


class InvitationConfirmation(TemplateView):
    template_name = 'team/confirmation_page.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        token = self.kwargs.get('token')
        invitation = get_object_or_404(Invitation, token=token)
        invitation.accept_invitation()
        team = invitation.team
        context['team'] = team
        return context
