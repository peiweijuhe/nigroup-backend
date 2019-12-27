from django.contrib import admin
from .models import Gallery


class GalleryAdmin(admin.ModelAdmin):
    list_display = ('title', 'image','key' )


# Register your models here.
admin.site.register(Gallery, GalleryAdmin)
