from django.urls import path
from .views import all_notes, note_detail

urlpatterns = [
    path('notes/', all_notes),
    path('notes/<int:id>', note_detail)
]