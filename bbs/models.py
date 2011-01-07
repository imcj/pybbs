#! coding:utf-8
from django.db import models
from django.contrib import admin

class Category(models.Model):
    name = models.CharField('名称' , max_length = 100)
    linkname = models.CharField('连接名' , max_length = 100)
    sort = models.IntegerField('排序' , max_length = 10 , default = 01)

class Thread(models.Model):
    pass

class Reply(models.Model):
    pass
