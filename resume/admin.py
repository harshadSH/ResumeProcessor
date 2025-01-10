from django.contrib import admin
from .models import Candidate

@admin.register(Candidate)
class CandidateAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'email', 'mobile_number')
    search_fields = ('first_name', 'email', 'mobile_number')
