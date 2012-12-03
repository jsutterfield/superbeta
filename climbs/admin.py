from django.contrib import admin
from models import Route, RoutePhoto
from models import Area, AreaPhoto

class RouteAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}

class AreaAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}

admin.site.register(Route, RouteAdmin)
admin.site.register(RoutePhoto)
admin.site.register(Area, AreaAdmin)
admin.site.register(AreaPhoto)
