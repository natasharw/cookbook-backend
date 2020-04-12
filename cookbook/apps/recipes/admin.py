from django.contrib import admin
from .models import Recipe, Timing

class TimingAdmin(admin.ModelAdmin):
    list_display = [f.name for f in Timing._meta.fields]

class RecipeAdmin(admin.ModelAdmin):
    list_display = [f.name for f in Recipe._meta.fields]

admin.site.register(Recipe, RecipeAdmin)
admin.site.register(Timing, TimingAdmin)