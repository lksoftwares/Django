from django.contrib import admin
from newschanel.models import NewsChanel
class NewsAdmin(admin.ModelAdmin):
        list_display=('newsTitle','newsInfo','newsImage')
admin.site.register(NewsChanel,NewsAdmin)    