from django.contrib import admin
from .models import Node,Gateway, Node_Data, Type

admin.site.register(Type)
admin.site.register(Node_Data)
admin.site.register(Node)
admin.site.register(Gateway)

# Register your models here.
