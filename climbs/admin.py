from django.contrib import admin
from models import Problem, ProblemPhoto
from models import Area, AreaPhoto

class AreaPhotoInline(admin.TabularInline):
    model = AreaPhoto

class ProblemPhotoInline(admin.TabularInline):
    model = ProblemPhoto

class AreaAdmin(admin.ModelAdmin):
    inlines = [
        AreaPhotoInline
    ]

class ProblemAdmin(admin.ModelAdmin):
    inlines = [
        ProblemPhotoInline
    ]

admin.site.register(Area, AreaAdmin)
admin.site.register(Problem, ProblemAdmin)