from django.db import models

# Create your models here.
class Pro_language(models.Model):
    name = models.CharField(
        max_length=30,
        verbose_name="编程语言名字"
    )
    theheat = models.IntegerField()
