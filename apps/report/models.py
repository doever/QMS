from django.db import models

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
    createdate = models.DateTimeField(auto_now_add=True,db_index=True,null=True)
    installdate = models.DateTimeField(db_index=True,null=True)
    installer = models.ForeignKey('account.User',on_delete=models.DO_NOTHING)
    a3 = models.CharField(max_length=10,null=True)
    A7 = models.CharField(max_length=10,null=True)
