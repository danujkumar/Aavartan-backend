from rest_framework import serializers
from server.models import Server


class ServerSerializer(serializers.ModelSerializer):

    class Meta:
        model = Server
        fields = ('id',
                  'title',
                  'description',
                  'published')
