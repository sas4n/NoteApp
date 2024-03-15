from rest_framework import serializers
from .models import Note
from django.contrib.auth.models import User
from rest_framework.authtoken.views import Token


class NoteSerializer(serializers.ModelSerializer):
   class Meta:
      model = Note
      fields = ['id', 'title', 'description']


class UserSerializer(serializers.ModelSerializer):
   class Meta:
      model = User
      fields = ['id', 'username', 'password']

      extra_kwargs = {
        'password': {
            'required': True,
            'write_only': True,
            }
        }

   def create(self, validated_data):
      user = User.objects.create_user(** validated_data)
      Token.objects.create(user=user)
      return user
      



   '''title = serializers.CharField(max_length=120)
    description = serializers.CharField(max_length=400)


    def create(self, validated_data):
        return Note.objects.create(validated_data)
    
    def update(self, instance, validated_data):
        instance.title = validated_data.get('title', instance.title)
        instance.description = validated_data.get('description', instance.description)('title', instance.title)'''

