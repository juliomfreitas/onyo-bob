from django.contrib import admin
from powerball_backend.models import Ticket, Prize


class TicketInline(admin.TabularInline):
    model = Ticket


class PrizeAdmin(admin.ModelAdmin):
    inlines = [
        TicketInline,
    ]

admin.site.register(Ticket)
admin.site.register(Prize, PrizeAdmin)
