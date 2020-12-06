from django.contrib import admin

# Register your models here.
from .models import Committee, Events

admin.site.register(Committee)
admin.site.register(Events)