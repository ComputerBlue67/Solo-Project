from django.contrib import admin

# Register your models here.
from .models import File, Menu_item, User

admin.site.register(User)
admin.site.register(File)
admin.site.register(Menu_item)