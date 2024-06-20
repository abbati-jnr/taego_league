
from django.urls import path
from .views import TeamListCreate, TeamDetail, InvitationConfirmation, InvitationListCreate


urlpatterns = [
    path('teams/', TeamListCreate.as_view(), name='team-list-create'),
    path('teams/<int:pk>/', TeamDetail.as_view(), name='team-detail'),
    path('invitation/', InvitationListCreate.as_view(), name='invitation-create'),
    path('accept-invitation/<str:token>/', InvitationConfirmation.as_view(), name='invitation-accept'),
]
