from django.contrib import admin

from .models import Diary


@admin.register(Diary)
class DiaryAdmin(admin.ModelAdmin):
    list_display = ("id", "content", "emotion", "date")
    fields = ("id", "content", "emotion", "date")
