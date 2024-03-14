from django.contrib import admin
from .models import Note

# Register your models here.
#admin.site.register(Note)
@admin.register(Note)
class NoteAdmin(admin.ModelAdmin):
    list_filter = ('title', 'description')
    list_display = ('title', 'description')