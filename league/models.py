from django.db import models
from django.contrib.auth import get_user_model
from team.models import Team

User = get_user_model()


class League(models.Model):
    name = models.CharField(max_length=255)
    logo = models.ImageField(upload_to='league_logos/')
    description = models.TextField()
    admin = models.ForeignKey(User, on_delete=models.CASCADE, related_name='leagues')
    teams = models.ManyToManyField(Team, related_name='league', blank=True)

    def __str__(self):
        return self.name


class Invitation(models.Model):
    league = models.ForeignKey(League, on_delete=models.CASCADE, related_name='invitations')
    team = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='invitations')
    date = models.DateField(auto_now_add=True)
    token = models.CharField(max_length=64, unique=True, blank=True, null=True)
    accepted = models.BooleanField(default=False)

    def __str__(self):
        return self.team.name

    def accept_invitation(self):
        self.accepted = True
        self.league.teams.add(self.team)
        self.save()
