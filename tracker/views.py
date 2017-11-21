from tracker.models import Countdown, Tomato
from tracker.serializers import CountdownSerializer, TomatoSerializer, UserSerializer
from tracker.permissions import IsUser, IsUserAccount
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
from rest_framework import permissions, viewsets, mixins
from rest_framework.response import Response

class CountdownViewSet(viewsets.ModelViewSet):
    """
    Allows for `list`, `create`, `retrieve`, `update`,
    and `destroy` actions for Countdowns.
    """
    queryset = Countdown.objects.all()
    serializer_class = CountdownSerializer
    permission_classes = (permissions.IsAuthenticated,
                          IsUser)

    def get_queryset(self):
        return self.queryset.order_by('due')

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class TomatoViewSet(viewsets.ModelViewSet):
    """
    Allows for `list`, `create`, `retrieve`, `update`,
    and `destroy` actions for Tomatoes.
    """
    queryset = Tomato.objects.all()
    serializer_class = TomatoSerializer
    permission_classes = (permissions.IsAuthenticated,
                          IsUser)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class UserViewSet(mixins.RetrieveModelMixin,
                  viewsets.GenericViewSet):
    """
    Allows for the `retrieve` action for users.
    """
    queryset = User.objects.all()
    permission_classes = (permissions.IsAuthenticated,
                          IsUserAccount)
