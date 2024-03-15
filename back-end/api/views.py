
from django.shortcuts import render,HttpResponse 
from .models import Note
from .serializer import NoteSerializer, UserSerializer
from django.http import JsonResponse
from rest_framework.parsers import JSONParser
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import APIView
from rest_framework.viewsets import ModelViewSet
from django.contrib.auth.models import User
from rest_framework.permissions import IsAuthenticated
# Create your views here.

class NoteViewSet(ModelViewSet):
    queryset = Note.objects.all()
    serializer_class = NoteSerializer
     permission_classes = [IsAuthenticated]

class UserViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer



'''
class NotesListView(APIView):

    def get(self, request):
        notes = Note.objects.all()
        serializer = NoteSerializer(notes, many=True)
        return Response(serializer.data) 
    
    def post(self, request):
        serializer = NoteSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class NoteDetailsView(APIView):
    def get_note(self, id):
        try:
            return Note.objects.get(id=id)
        except Note.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
    
    def get(self, request, id):
        note = self.get_note(id)
        serializer = NoteSerializer(note)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def put(self, request, id):
        note = self.get_note(id)
        serializer = NoteSerializer(note, data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, id):
        note = self.get_note(id)
        note.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

'''
        
    

'''
@api_view(['GET', 'POST'])
def all_notes(request):

    if request.method == 'GET':
        notes = Note.objects.all()
        serializer = NoteSerializer(notes, many=True)
        return Response(serializer.data)
    
    elif request.method == 'POST':
        serializer = NoteSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

@api_view(['GET', 'PUT', 'DELETE'])
def note_detail(request, id):
    try:
        note = Note.objects.get(id=id)
    except Note.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        serializer = NoteSerializer(note)
        return Response(serializer.data, status=status.HTTP_200_OK)

    elif request.method == 'PUT':
        serializer = NoteSerializer(note, date = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        note.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
'''
    

