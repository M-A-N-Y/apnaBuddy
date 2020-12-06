from django.contrib import admin

# Register your models here.
from .models import Student,LostProperty,Portfolio,Academic,Subject,Feedback

admin.site.register(Student)
admin.site.register(LostProperty)
admin.site.register(Portfolio)
admin.site.register(Academic)
admin.site.register(Subject)
admin.site.register(Feedback)
# admin.site.register()
# admin.site.register()