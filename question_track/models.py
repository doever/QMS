from django.db import models
from django.contrib.auth.models import User
import datetime
# Create your models here.
class Documentname(models.Model):
    class Meta:
        verbose_name='文档字典'
        verbose_name_plural='文档字典'

    doctype = models.CharField(max_length=100,null=False)
    docname = models.CharField(max_length=100,unique=True,null=False,db_index=True)
    fatherid = models.IntegerField()
    createdate = models.DateTimeField(null=False, auto_now=True, db_index=True)

    def __str__(self):
        return self.docname


class QuestionState(models.Model):
    class Meta:
        verbose_name = '项目状态'
        verbose_name_plural = '项目状态'
    statetype = models.CharField(max_length=100,null=False)
    statecode= models.IntegerField(default=1,unique=True)
    statename = models.CharField(max_length=100,db_index=True)
    fatherid = models.IntegerField()
    allow = models.CharField(max_length=200)
    createdate = models.DateTimeField(null=False, auto_now=True, db_index=True)

    def __str__(self):
        return self.statename

class QuestionClass(models.Model):
    class Meta:
        verbose_name = '问题分类'
        verbose_name_plural = '问题分类'

    classtype = models.CharField(max_length=100)
    classname = models.CharField(max_length=100,db_index=True)
    createdate = models.DateTimeField(null=False, auto_now=True, db_index=True)

    def __str__(self):
        return self.classname

class Question(models.Model):
    class Meta:
        verbose_name = '问题'
        verbose_name_plural = '问题'

    #设置默认解决时间为本周最后一天
    DEFAULT_SOLVEDATE=datetime.datetime.now()+datetime.timedelta(days=5)
    LEVEL_CHOICES=(
        (1,'普通'),
        (2,'一般'),
        (3,'严重'),
        (4,'紧急'),
    )

    creator = models.ForeignKey(User,on_delete=models.CASCADE,related_name='creator_User')
    createdate = models.DateTimeField(null=False,auto_now=True,db_index=True)
    principal = models.ForeignKey(User,on_delete=models.CASCADE,related_name='principal_User')
    solvedate = models.DateTimeField(null=False,default=DEFAULT_SOLVEDATE,db_index=True)
    #问题名字不能为空
    questionname = models.CharField(max_length=200, unique=True,blank=False)
    #问题描述不能用null值
    questiondesc = models.TextField(max_length=1000,null=False)
    questionclass = models.ForeignKey(QuestionClass,on_delete=models.CASCADE)
    questionlevel = models.CharField(max_length=100,choices=LEVEL_CHOICES,default='普通')
    questionsource = models.CharField(max_length=100,null=False)
    questionstate = models.ForeignKey(QuestionState,on_delete=models.CASCADE,db_index=True)
    connectoremail = models.EmailField(max_length=254,default='ctt@toowell.cn')
    isclean = models.BooleanField(default=False)
    isdel = models.BooleanField(default=False)
    isspecial = models.NullBooleanField(default=False)
    # uploadfile=models.FileField(upload_to='staticfile/uploads/%Y/%m/%d')

    def __str__(self):
        return self.questionname


class Solution(models.Model):
    class Meta:
        verbose_name='解决办法'
        verbose_name_plural='解决办法'

    questionid = models.ForeignKey(Question,on_delete=models.CASCADE)
    creator = models.ForeignKey(User,on_delete=models.CASCADE)
    createdate = models.DateTimeField(auto_now=True,db_index=True)
    solutionname = models.CharField(max_length=200, unique=True,blank=False)
    solutiondesc = models.TextField(max_length=1000,null=False)
    isdel = models.BooleanField(default=False)
    isspecial = models.NullBooleanField(default=False)

    def __str__(self):
        return self.solutionname

class Applynew(models.Model):
    class Meta:
        verbose_name='开户单'
        verbose_name_plural='开户单'
    billno = models.CharField(max_length=50,null=False,db_index=True,unique=True)
    machinesid = models.CharField(max_length=50,db_index=True,null=True)
    name = models.CharField(max_length=50,null=True)
    province = models.CharField(max_length=20,null=True)
    city = models.CharField(max_length=20,null=True)
    area = models.CharField(max_length=20,null=True)
    billstate = models.IntegerField(db_index=True,null=True)
    billsort = models.CharField(max_length=20,null=True)
    isspecial = models.CharField(max_length=10,null=True)
    agent = models.IntegerField(null=True)
    areacode = models.CharField(max_length=30,db_index=True,null=True)
    creayedate = models.DateTimeField(db_index=True,null=True)
    installdate = models.DateTimeField(db_index=True,null=True)
    a3 = models.CharField(max_length=10,null=True)
    A7 = models.CharField(max_length=10,null=True)



