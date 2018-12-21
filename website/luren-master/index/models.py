import datetime

from django.db import models
from django.urls import reverse

# Create your models here.

class User(models.Model):
    u_name = models.CharField(max_length=30)
    u_pwd = models.CharField(max_length=30)
    u_email = models.EmailField(null=True)
    u_phone = models.CharField(max_length=20)
    u_gender = models.CharField(max_length=10, null=True)
    u_portrait = models.CharField(max_length=500, default="/static/img/default.jpg/")
    u_profile = models.TextField(default="用户没有填写任何个人信息...")
    u_is_active = models.BooleanField(default=True)
    u_time = models.CharField(max_length=30, verbose_name='注册时间', null=True)
    u_address = models.CharField(max_length=50, verbose_name='地址', null=True)

    def __str__(self):
        return self.u_name
    def __unicode__(self):
        return self.u_name

    def to_dict(self):
        dic = {
            "id": self.id,
            "ugender": self.u_gender,
            "uphone": self.u_phone,
            "uname": self.u_name,
            "uemail": self.u_email,
            "uportrait": self.u_portrait,
            "uprofile": self.u_profile,
            "utime": self.u_time,
            "uaddress": self.u_address,
            "isActive": self.u_is_active
        }
        return dic

class Article(models.Model):
    # 外键
    u_id = models.ForeignKey(User,on_delete=None)


    a_title = models.CharField(max_length=50)
    a_content = models.TextField()
    a_time = models.DateTimeField(null="True")
    a_is_active = models.BooleanField(default=True)
    a_cover = models.CharField(max_length=500, null=True)
    a_page_views = models.IntegerField(default=0)
    a_like_num = models.IntegerField(default=0)
    a_collect = models.IntegerField(default=0)
    a_read_count = models.IntegerField(max_length=10, default=0)
    a_comment_count = models.IntegerField(max_length=6, default=0)
    updated = models.DateTimeField(auto_now=True, auto_now_add=False)

    def __unicode__(self):
        return self.a_title
    def __str__(self):
        return self.a_title

    def get_absolute_url(self):
        return reverse("article",kwargs={"id":self.id})
        # return "/article/a_id=%s/" %(self.id)
    class Meta:
        ordering = ["-a_time","-updated"]



    def to_dict(self):
        dic = {
            'article_id': self.id,
            'title': self.a_title,
            'content': self.a_content,
            'datatime': self.a_time,
            'cover': self.a_cover,
            'read_count': self.a_read_count,
            'comment_count': self.a_comment_count,
            'is_active': self.a_is_active,
        }
        return dic


class Comment(models.Model):
    # 外键
    a_id = models.ForeignKey(Article,on_delete=None)  # 文章的id  而且，文章发布者的id也可从这取
    from_uid = models.ForeignKey(User,on_delete=None) # 评论者id



    c_text = models.TextField()
    c_image = models.CharField(max_length=500)
    c_time = models.DateTimeField()
    c_is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.c_text


class Reply(models.Model):
    # 外键
    c_id = models.ForeignKey(Comment,on_delete=None)  # 被回复的评论id
    from_uid = models.ForeignKey(User,on_delete=None) # 回复者id
    to_uid = models.IntegerField() # 被回复者id

    r_text = models.TextField()
    r_image = models.CharField(max_length=500)
    r_time = models.DateTimeField()
    r_is_active = models.BooleanField(default=True)
    r_type = models.CharField(max_length=30, null=True) # 回复类型
    r_type_id = models.IntegerField(null=True) # 对应回复类型下的目标id（可能是对评论id的回复，也可能是对回复id的回复）

    def __str__(self):
        return self.r_text


class Test(models.Model):
    t_title = models.CharField(max_length=30, default="kerwin")
    t_text = models.CharField(max_length=30, default="0")

    def __str__(self):
        return self.t_title

















