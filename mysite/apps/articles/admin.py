from django.contrib import admin

from .models import Article_AD, Article_PG, Comment_AD, Comment_PG

admin.site.register(Article_AD)
admin.site.register(Article_PG)
admin.site.register(Comment_AD)
admin.site.register(Comment_PG)
