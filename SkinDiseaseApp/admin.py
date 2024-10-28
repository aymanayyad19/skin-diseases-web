from django.contrib import admin
from .models import SkinDisease




@admin.register(SkinDisease)
class SkinDiseaseAdmin(admin.ModelAdmin):
    list_display = ('name', 'created_at', 'updated_at')
    search_fields = ('name', 'symptoms', 'risk_factors')
    list_filter = ('created_at', 'updated_at')
    ordering = ('name',)
