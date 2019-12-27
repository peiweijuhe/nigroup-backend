from django.contrib import admin
from .models import Research


class ResearchAdmin(admin.ModelAdmin):
    list_display = ('link', 'image', 'title', 'content1', 'content2', 'content3')


# Register your models here.
admin.site.register(Research, ResearchAdmin)
