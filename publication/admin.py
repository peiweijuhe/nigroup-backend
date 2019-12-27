from django.contrib import admin
from .models import Publication


class PublicationAdmin(admin.ModelAdmin):
    list_display = ('author', 'title', 'link', 'press', 'issue', 'year')


# Register your models here.
admin.site.register(Publication, PublicationAdmin)
