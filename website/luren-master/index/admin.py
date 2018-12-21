from django.contrib import admin
from .models import *

class UserAdmin(admin.ModelAdmin):
    list_display = ["u_name", "u_pwd","u_phone", "u_gender", "u_is_active", "u_portrait"]
    # list_filter = ["gender"]
    search_fields = ["u_name"]


class ArticleAdmin(admin.ModelAdmin):
    list_display = ["id", "a_title", "a_page_views", "a_time", "a_is_active"]
    list_filter = ["a_time"]
    search_fields = ["a_title", "a_content"]

class CommentAdmin(admin.ModelAdmin):
    list_display = ["c_time", "c_is_active"]

class ReplyAdmin(admin.ModelAdmin):
    list_display = ["r_time", "r_is_active", "r_type", "r_type_id", "to_uid"]

class TestAdmin(admin.ModelAdmin):
    list_display = [ "t_title", "t_text"]


admin.site.register(User, UserAdmin)
admin.site.register(Article, ArticleAdmin)
admin.site.register(Comment, CommentAdmin)
admin.site.register(Reply, ReplyAdmin)
admin.site.register(Test, TestAdmin)
