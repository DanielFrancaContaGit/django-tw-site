from django.contrib.auth.models import Group, User
from rest_framework import serializers
from core.models import Produtos


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']


class ProdutosSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Produtos
        fields = '__all__' 


