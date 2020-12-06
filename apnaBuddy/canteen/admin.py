from django.contrib import admin

# Register your models here.


#from .models import *
from .models import Manager, Order, Menu

admin.site.register(Manager)
admin.site.register(Order)
admin.site.register(Menu)
#admin.site.register()
