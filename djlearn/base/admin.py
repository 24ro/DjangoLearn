from django.contrib import admin
from django.contrib.admin.sites import AlreadyRegistered

# Register your models here.
from .models import Room, Topic, Message

try:
    admin.site.register(Room)
except AlreadyRegistered:
    pass
try:
    admin.site.register(Topic)
except AlreadyRegistered:
    pass
try:
    admin.site.register(Message)
except AlreadyRegistered:
    pass