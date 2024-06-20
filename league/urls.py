
from django.urls import path
from .views import LeagueListCreate, LeagueDetail, InvitationListCreate, InvitationConfirmation


urlpatterns = [
    path('leagues/', LeagueListCreate.as_view(), name='league-list-create'),
    path('leagues/<int:pk>/', LeagueDetail.as_view(), name='league-detail'),
    path('invitation/', InvitationListCreate.as_view(), name='invitation-create'),
    path('accept-invitation/<str:token>/', InvitationConfirmation.as_view(), name='invitation-accept'),
]
