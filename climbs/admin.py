from django.contrib import admin
from models import Route, Photo

class RouteAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}

admin.site.register(Route, RouteAdmin)
admin.site.register(Photo)
