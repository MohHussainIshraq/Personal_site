from django.contrib import admin
from . models import Article, Comment

# Register your models here.
admin.site.site_header = "مدیریت وبلاگ من"
admin.site.site_title = "سپیده"
admin.site.register(Article)
admin.site.register(Comment)
