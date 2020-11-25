from django.contrib import admin
from .models import connection,thread

# Register your models here.
class adminconnection(admin.ModelAdmin):
    filter_horizontal=('connections',)

admin.site.register(connection,adminconnection)
admin.site.register(thread)