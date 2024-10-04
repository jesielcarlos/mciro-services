from system1.apps.core.models import Users
from system1.apps.core.repositories.user_repository import UserRepository
from system1.apps.core.serializers import UsersSerializerList
from rest_framework.response import Response
from rest_framework import viewsets


class UsersViewSet(viewsets.ViewSet):
    queryset = Users.objects.all()
    serializer_class = UsersSerializerList
    repository = UserRepository

    def list(self, request):
        users = self.repository.find_all()
        serializer = UsersSerializerList(users, many=True)
        data = serializer.data

        return Response(data)
    
    