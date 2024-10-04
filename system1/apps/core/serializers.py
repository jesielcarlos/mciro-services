from rest_framework import serializers
from system1.apps.core.models import Users


class UsersSerializerList(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = "__all__"
