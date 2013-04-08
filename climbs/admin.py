from django.contrib import admin
from models import Route, RoutePhoto
from models import Area, AreaPhoto

class AreaPhotoInline(admin.TabularInline):
    model = AreaPhoto

class RoutePhotoInline(admin.TabularInline):
    model = RoutePhoto

class AreaAdmin(admin.ModelAdmin):
    inlines = [
        AreaPhotoInline
    ]

class RouteAdmin(admin.ModelAdmin):
    inlines = [
        RoutePhotoInline
    ]

admin.site.register(Area, AreaAdmin)
admin.site.register(Route, RouteAdmin)