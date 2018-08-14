from django.db import models

# Create your models here.
class Firecart(models.Model):
    name = models.CharField(max_length=30,verbose_name="名字")
    speed = models.IntegerField(verbose_name="时速",default=30,db_column="myspeed")
    creat_date = models.DateTimeField(
        auto_now=True,
        verbose_name="出厂日期"
    )
    last_updata= models.DateField(
        auto_now=True
    )
    is_used = models.BooleanField(default=True,verbose_name="是否在用")
    class Meta:
        verbose_name = "火车类"
        db_table = "huocart"