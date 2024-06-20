from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class Team(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    logo = models.ImageField(upload_to='team_logos/', blank=True, null=True)
    team_manager = models.ForeignKey(User, blank=True, null=True, on_delete=models.SET_NULL, related_name='teams')
    players = models.ManyToManyField(User, related_name='player', blank=True, null=True)

    def __str__(self):
        return self.name


class Invitation(models.Model):
    email = models.EmailField()
    team = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='player_invitations')
    date = models.DateField(auto_now_add=True)
    token = models.CharField(max_length=64, unique=True, blank=True, null=True)
    accepted = models.BooleanField(default=False)

    def __str__(self):
        return self.team.name

    def accept_invitation(self):
        self.accepted = True
        self.save()
