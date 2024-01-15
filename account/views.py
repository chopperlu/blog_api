import permission
from dj_rest_auth.views import LogoutView
from django.contrib.auth.models import User
from rest_framework import generics, permissions
from rest_framework.viewsets import GenericViewSet
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.mixins import ListModelMixin, RetrieveModelMixin

from like.serializers import FavoriteSerializer
from post.permission import IsOwner, IsOwnerOrAdmin
from . import serializers

#
class UserRegisterView(generics.CreateAPIView):
    serializer_class = serializers.RegisterSerializer

class CustomLogoutView(LogoutView):
    permission_classes = (permissions.IsAuthenticated,)


class UserViewSet(RetrieveModelMixin, ListModelMixin, GenericViewSet):
    queryset = User.objects.all()
    permission_classes = (permissions.IsAuthenticated,)

    def get_serializer_class(self):
        if self.action == 'list':
            return serializers.UserListSerializer
        return serializers.UserDetailSerializer
#

    @action(['GET'], detail=False)
    def favorites(self, request):
        user = request.user
        favorites = user .favorites.all()
        serializer = FavoriteSerializer(favorites, many=True)
        return Response(serializer.data, status=200)





# class UserListView(generics.ListAPIView):
#     queryset = User.objects.all()
#     serializer_class = serializers.UserListSerializer
#     permission_classes = (permissions.IsAuthenticated,)
#
#
# class UserDetailView(generics.RetrieveAPIView):
#     queryset = User.objects.all()
#     serializer_class = serializers.UserListSerializer
#     permission_classes = (permissions.IsAuthenticated,)


