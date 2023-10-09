from django.contrib import admin

# Register your models here.
# import uuid
# print(uuid.uuid4())

from .models import Room, Message

admin.site.register(Room)
admin.site.register(Message)