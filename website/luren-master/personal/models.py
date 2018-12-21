from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField

# Create your models here.
# Create your models here.
class BlogEditor(models.Model):
    title = models.CharField(max_length = 50,verbose_name = '标题')
    content = RichTextUploadingField(verbose_name = "正文",config_name = 'luren_ckeditor')
