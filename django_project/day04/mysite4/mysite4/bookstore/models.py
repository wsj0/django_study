from django.db import models

# Create your models here.

class Book(models.Model):
    #varchar(30)
    title=models.CharField(max_length=30,
                           null=False,
                           unique=True,
                           verbose_name='书名')
    pub=models.CharField(max_length=50,
                         null=True,
                         verbose_name='出版社',
                         )
    #decimal(7,2)
    price=models.DecimalField(
        decimal_places=2,
        max_digits=7,
        default=9999,
        verbose_name='定价')
    market_price=models.DecimalField(
        decimal_places=2,
        max_digits=7,
        default=9999,
        verbose_name='零售价')

class Author(models.Model):
    name=models.CharField(max_length=30,
                          verbose_name="姓名")
    age=models.IntegerField(verbose_name="年龄")
    email=models.EmailField(null=True,verbose_name="邮箱")
