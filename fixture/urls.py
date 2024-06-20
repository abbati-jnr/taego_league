
from django.urls import path
from .views import FixtureListCreate, FixtureDetail


urlpatterns = [
    path('fixtures/', FixtureListCreate.as_view(), name='fixture-list-create'),
    path('fixtures/<int:pk>/', FixtureDetail.as_view(), name='fixture-detail'),
]
