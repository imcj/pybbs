#! coding:utf-8
from django.db import models
from django.contrib.auth.models import User

# 彪哥，虽然你的习惯是在model里面加入admin
# but，Django的约束是放在admin.py 里面。
# 我不想说明神马，只是希望这次你就依了我吧。

# 彪哥必看
# 关于我加入的south app 这是在Django里面的migration
# 你也不想每次都要先删除数据库以后 manager.py syncdb吧？
# 所以给你总结出来就是
# ./manage.py schemamigration [app] --auto
# ./manage.py migrate [app]
# 有神马问题立刻联系我，如果没有问题，表示同意的话请删除注释

class Category(models.Model):
    name = models.CharField('名称' , max_length = 100)
    slug = models.SlugField ( u"短地址", max_length = 100 )
    sort = models.IntegerField('排序' , max_length = 10 , default = 01)

class Thread(models.Model):
    cate = models.ForeignKey(Category)
    slug = models.SlugField ( u"短地址", max_length = 100, null = True, blank = True )
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
