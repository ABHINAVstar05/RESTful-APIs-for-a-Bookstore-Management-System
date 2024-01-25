from rest_framework import serializers

from app.models import *


class bookDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = bookDetails
        fields = '__all__'


class usersSerializer(serializers.ModelSerializer):
    class Meta:
        model = users
        fields = '__all__'
