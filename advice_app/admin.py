from django.contrib import admin
from .models import Post

# Register your models here.
@admin.register(Post)
class PostAdmnin(admin.ModelAdmin):
    list_display = ['content','date_posted','author']
    list_filter = []
    search_fields = []
