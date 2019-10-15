from titles.models import Title
from titles.serializers import TitleSerializer
from django.http import Http404
from rest_framework.generics import CreateAPIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated


class CreateTitleView(CreateAPIView):
    """
    Create a new title
    """
    permission_classes = (IsAuthenticated, )
    serializer_class = TitleSerializer

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
