from rest_framework import serializers
from .models import Note

class NoteSerializer(serializers.ModelSerializer):
   class Meta:
      model = Note
      fields = ['id', 'title', 'description']
   '''title = serializers.CharField(max_length=120)
    description = serializers.CharField(max_length=400)


    def create(self, validated_data):
        return Note.objects.create(validated_data)
    
    def update(self, instance, validated_data):
        instance.title = validated_data.get('title', instance.title)
        instance.description = validated_data.get('description', instance.description)('title', instance.title)'''

