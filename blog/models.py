# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Article(models.Model):
    title =models.CharField(max_length=255)
    text =models.TextField()

    def __unicode__(self):
        return self.title

    def get_abstract(self):
        return ' '.join(self.text.split()[1:20])+' ...'


    @models.permalink
    def get_absolute_url(self):
        return ('article-detail',[self.id])
class Comment(models.Model):
    article = models.ForeignKey('Article')
    text = models.TextField(verbose_name='Ваш комментарий')
    image = models.ImageField(blank='True',null=True)
