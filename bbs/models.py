from django.db import models
from django.contrib.auth.models import User

# 帖子表
class Article(models.Model):
    #标题
    title = models.CharField(u"帖子标题",max_length=225,unique=True)
    #上传文件(图片...)
    head_img = models.ImageField(upload_to="uploads")
    #作者
    author = models.ForeignKey("User",verbose_name="作者")
    #内容
    content = models.TextField(u"内容")
    #类型
    type = models.ForeignKey("type",verbose_name='板块名称')
    #发布时间
    publish_data = models.DateTimeField(auto_now=True,verbose_name="发布时间")
    #点赞个数
    poll_count = models.IntegerField(default=0,verbose_name="点赞个数")
    #评论数
    comment_count = models.IntegerField("Comment",default=0,verbose_name="评论个数")

#用户表
class User(models.Model):
    pass
#评论表
class Comment(models.Model):
    pass
#板块类型表
class type(models.Model):
    pass