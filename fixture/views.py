from rest_framework import generics
from .models import Fixture
from .serializers import FixtureSerializer


class FixtureListCreate(generics.ListCreateAPIView):
    queryset = Fixture.objects.all()
    serializer_class = FixtureSerializer


class FixtureDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Fixture.objects.all()
    serializer_class = FixtureSerializer
