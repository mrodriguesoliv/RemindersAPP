from django.contrib import admin
from .models import Conversation, Interaction, Reminder

@admin.register(Conversation)
class ConversationAdmin(admin.ModelAdmin):
    list_display = ('conversation_id', 'user', 'created_at')
    search_fields = ('conversation_id', 'user__username')


@admin.register(Interaction)
class InteractionAdmin(admin.ModelAdmin):
    list_display = ('conversation', 'prompt', 'response')
    list_filter = ('conversation',)


@admin.register(Reminder)
class ReminderAdmin(admin.ModelAdmin):
    list_display = ('event', 'description', 'location')
    search_fields = ('event',)