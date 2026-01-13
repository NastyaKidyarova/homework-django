from django.contrib import admin
from .models import Feedback

@admin.register(Feedback)
class FeedbackAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'email', 'checked', 'text')
    list_filter = ('checked',)
    search_fields = ('full_name', 'email')
