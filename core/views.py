from django.contrib.auth.models import Group, User
from rest_framework import permissions, viewsets, status
from rest_framework.views import APIView
from rest_framework.response import Response

from core.serializers import GroupSerializer, UserSerializer, ProdutosSerializer
from core.models import Produtos


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticated]


class ProdutosViewSet(APIView):

    def get(self, request):
        produtoList = Produtos.objects.all()

        produtosListSerializer = ProdutosSerializer(produtoList, many=True)

        return Response(produtosListSerializer.data, status=status.HTTP_200_OK)

