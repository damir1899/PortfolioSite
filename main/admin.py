from django.contrib import admin
from .models import UserMessage, Projects, Category

@admin.register(UserMessage)
class UserMessageAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'subject']
    
admin.site.register(Category)
admin.site.register(Projects)
    
