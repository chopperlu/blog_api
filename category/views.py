from rest_framework import generics, permissions
from . import serializers
from category.models import Category


class CategoryCreateListView(generics.ListCreateAPIView):
    queryset = Category.objects.all()


    def get_serializer_class(self):
        if self.request.method == 'GET':
            return serializers.CategoryListSerializer
        return serializers.CategorySerializer

    def get_permissions(self):
        if self.request.method == 'GET':
            return [permissions.AllowAny(),]
        return [permissions.IsAdminUser(),]


class CategoryDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = serializers.CategorySerializer

    def get_permissions(self):
        if self.request.method == 'GET':
            return [permissions.AllowAny(), ]
        return [permissions.IsAdminUser(), ]
