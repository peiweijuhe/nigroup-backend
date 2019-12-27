from django.contrib import admin
from .models import People


class PeopleAdmin(admin.ModelAdmin):
    list_display = ('name', 'title', 'email', 'project', 'address', 'experience', 'completed','headshot')


# Register your models here.
admin.site.register(People, PeopleAdmin)
