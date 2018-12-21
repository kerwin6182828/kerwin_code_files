from django.contrib import admin

# Register your models here.

from django import forms
from django.contrib import admin
from ckeditor_uploader.widgets import CKEditorUploadingWidget

from .models import *

class BlogEditorAdminForm(forms.ModelForm):
    cover_image = forms.CharField(max_length = 200,
                                  label='首页配图',
                                  widget = forms.TextInput(
                                      attrs = {
                                          'placeholder':'点击源码复制图片链接',
                                      }
                                  )
                                  )
    content = forms.CharField(label = '正文',widget=CKEditorUploadingWidget(config_name = 'luren_ckeditor'))
    class Meta:
        model = BlogEditor
        fields = '__all__'


class BlogEditorAdmin(admin.ModelAdmin):
    form = BlogEditorAdminForm


admin.site.register(BlogEditor, BlogEditorAdmin)
