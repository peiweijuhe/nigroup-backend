from django.contrib import admin
from .models import News


class NewsAdmin(admin.ModelAdmin):
    list_display = ('link', 'date','content' )


# Register your models here.
admin.site.register(News, NewsAdmin)
