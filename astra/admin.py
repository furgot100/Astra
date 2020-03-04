from django.contrib import admin
from astra.models import Blog

# Register your models here.
class BlogAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'created', 'modified')

admin.site.reqister(Blog, BlogAdmin)