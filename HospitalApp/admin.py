from django.contrib import admin
from .models import Hospital, History


@admin.register(Hospital)
class HospitalAdmin(admin.ModelAdmin):
    list_display = ('name', 'city', 'contact_number',  'created_at', 'updated_at')
    search_fields = ('name', 'city')
    list_filter = ( 'city','contact_number')
    ordering = ('name',)


@admin.register(History)
class HistoryAdmin(admin.ModelAdmin):
    list_display = ('image_url', 'user__email', 'created_at', 'updated_at')
    search_fields = ('image_url', 'user__email')
    list_filter = ('user__email',)
    ordering = ('-created_at',)
