
#coding:utf8
from __future__ import unicode_literals
from DjangoUeditor.models import UEditorField
from django.db import models


# Create your models here.

class Article(models.Model):
    title = models.CharField(u"博客标题",max_length = 100)
    category = models.CharField(u"博客标签",max_length = 50,blank = True)
    pub_date = models.DateTimeField(u"发布日期",auto_now_add = True,editable=True)
    update_time = models.DateTimeField(u'更新时间',auto_now=True,null=True)
    content = UEditorField(u"文章正文", height=300, width=1000, default=u'', blank=True, imagePath="uploads/web/images/",
                           toolbars='besttome', filePath='uploads/web/files/')
    def __unicode__(self):
        return self.title

    class Meta:
        ordering = ['-pub_date']
        verbose_name = "文章"
        verbose_name_plural = "文章"

