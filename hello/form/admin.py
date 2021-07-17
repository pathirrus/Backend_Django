from django.contrib import admin
from form.models import Message

# Register your models here.
# admin.site.register(Message)


# modyfikacja widoku panelu administratora:

@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = ["id", "name", "email", "body"]
    ordering = ["name"]
