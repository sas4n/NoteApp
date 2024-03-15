from django.urls import path, include
from .views import NoteViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('notes', NoteViewSet, basename='notes' )

urlpatterns = [
    path('', include(router.urls))
   # path('notes/', ),
   # path('notes/<int:id>', )
    #path('notes/', all_notes),
    #path('notes/<int:id>', note_detail)
]