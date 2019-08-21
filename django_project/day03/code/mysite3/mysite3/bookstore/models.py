from django.db import models

# Create your models here.

class Book(models.Model):
    #varchar(30)
    title=models.CharField(max_length=30,
                           null=False,
                           unique=True,
                           verbose_name='书名')
    #decimal(7,2)
    price1=models.DecimalField(decimal_places=2,
                              max_digits=7,
                               null=True,
                               verbose_name='定价')
    price2=models.DecimalField(decimal_places=2,
                               null=True,
                              max_digits=7,verbose_name='零售价')

class Author(models.Model):
    name=models.CharField(max_length=30,
                          null=False,
                          verbose_name="姓名")
    age=models.IntegerField(null=False,
                            default=1,
                            verbose_name="年龄")
    email=models.EmailField(max_length=100,
                            null=True,
                            verbose_name="邮箱")
