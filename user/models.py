from datetime import datetime
from django.db import models


# Create your models here.

class User(models.Model):
    SEX = (
        ('male', '男性'),
        ('female', '女性')
    )
    LOCATION = (
        ('bj', '北京'),
        ('sh', '上海'),
        ('gz', '广州'),
        ('sz', '深圳'),
        ('lz', '兰州'),
        ('xa', '西安'),
        ('cq', '重庆'),
        ('cd', '成都'),
        ('zz', '郑州')
    )
    phonenum = models.CharField(max_length=16, unique=True, verbose_name='手机号')

    nickname = models.CharField(max_length=32, verbose_name='昵称')

    sex = models.CharField(max_length=8, choices=SEX, verbose_name='性别')

    birth_day = models.DateTimeField(default=datetime(2000, 1, 1), verbose_name='出生日期')

    avatar = models.CharField(max_length=256, verbose_name='个人形象')

    location = models.CharField(max_length=8, verbose_name='长居地')







