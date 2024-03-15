from django.urls import path, include
from .views import NoteViewSet, AuthViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('notes', NoteViewSet, basename='notes' )
router.register('auth', AuthViewSet)

urlpatterns = [
    path('', include(router.urls))
   # path('notes/', ),
   # path('notes/<int:id>', )
    #path('notes/', all_notes),
    #path('notes/<int:id>', note_detail)
]