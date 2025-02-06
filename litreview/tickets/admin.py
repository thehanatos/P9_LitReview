from django.contrib import admin
from .models import Ticket

@admin.register(Ticket)
class TicketAdmin(admin.ModelAdmin):
    list_display = ('book_title', 'user', 'created_at')
    search_fields = ('book_title', 'user__username')
