from django.db import models

# Create your models here.
class Thegun(models.Model):
    name = models.CharField(
        max_length=30,
        verbose_name="枪的名字"
    )
    capacity = models.IntegerField(
        verbose_name="弹夹容量"
    )
    date = models.DateTimeField(
        auto_now_add=True,
        verbose_name="生产日期"
    )
    class Meta:
        verbose_name = "表名"
        db_table = "枪"
