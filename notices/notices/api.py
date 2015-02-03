from django.contrib.auth.models import User
from rest_framework import serializers, viewsets
from .models import Profile, Roles, RolePermissions


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'is_staff')

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class ProfileSerializer(serializers.HyperlinkedModelSerializer):
    
    class Meta:
        model = Profile
        fields = ('url','user','name','roles')

class RoleSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Roles
        fields = ('url', 'title', 'permissions')
class PermissionSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = RolePermissions
        fields = ('url','title')

class ProfileViewSet(viewsets.ModelViewSet):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer

class RoleViewSet(viewsets.ModelViewSet):
    queryset = Roles.objects.all()
    serializer_class = RoleSerializer

class RolePermissionsViewSet(viewsets.ModelViewSet):
    queryset = RolePermissions.objects.all()
    serializer_class = PermissionSerializer
