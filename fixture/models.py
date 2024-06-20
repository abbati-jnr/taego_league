from django.db import models
from team.models import Team
from league.models import League


class Fixture(models.Model):
    league = models.ForeignKey(League, on_delete=models.CASCADE, related_name='fixtures')
    team1 = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='team1_fixtures')
    team2 = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='team2_fixtures')
    date = models.DateField()
    time = models.TimeField()
    location = models.CharField(max_length=255)

    def __str__(self):
        return self.league.name
