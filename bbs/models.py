#! coding:utf-8
from django.db import models
from django.contrib.auth import User
#from django.contrib import admin

class Category(models.Model):
    name = models.CharField('名称' , max_length = 100)
    slug = models.SlugField ()
    sort = models.IntegerField('排序' , max_length = 10 , default = 01)

class Thread(models.Model):
    cate = models.ForeignKey(Category)
    title = models.CharField('标题' , max_length = 255)
    user = models.ForeignKey(User)
    content = models.TextField('内容')
    hits = models.IntegerField('浏览量' , default = 0)
    create_at = models.DateTimeField('发表时间')
    update_at = models.DateTimeField('最后修改时间')

class Reply(models.Model):
    thread = models.ForeignKey(Thread)
    user = models.ForeignKey(User)
    content = models.TextField('内容')
    create_at = models.DateTimeField('发表时间')
    update_at = models.DateTimeField('最后修改时间')
