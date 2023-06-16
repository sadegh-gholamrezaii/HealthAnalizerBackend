from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    COMMON = 1
    ADVANCE = 2
    TYPES = [
        (COMMON, 'common'),
        (ADVANCE, 'advance')
    ]
    type = models.PositiveSmallIntegerField(default=COMMON, choices=TYPES)


class Bmi(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='bmis')
    weight = models.CharField(max_length=10)
    height = models.CharField(max_length=10)
    result = models.CharField(max_length=80)
    created_time = models.DateField(auto_now_add=True)


class Bmr(models.Model):
    MALE = 1
    FEMALE = 2
    GENDER = (
        (MALE, 'male'),
        (FEMALE, 'female')
    )
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='bmrs')
    age = models.CharField(max_length=10)
    weight = models.CharField(max_length=10)
    height = models.CharField(max_length=10)
    gender = models.SmallIntegerField(choices=GENDER, default=MALE)
    result = models.CharField(max_length=80)
    created_time = models.DateField(auto_now_add=True)


class Whr(models.Model):
    MALE = 1
    FEMALE = 2
    GENDER = (
        (MALE, 'male'),
        (FEMALE, 'female')
    )
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='whrs')
    waist = models.CharField(max_length=10)
    hip = models.CharField(max_length=10)
    gender = models.SmallIntegerField(choices=GENDER, default=MALE)
    result = models.CharField(max_length=80)
    created_time = models.DateField(auto_now_add=True)


class Bfp(models.Model):
    MALE = 1
    FEMALE = 2
    GENDER = (
        (MALE, 'male'),
        (FEMALE, 'female')
    )
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='bfps')
    height = models.CharField(max_length=10)
    waist = models.CharField(max_length=10)
    hip = models.CharField(max_length=10)
    neck = models.CharField(max_length=10)
    gender = models.SmallIntegerField(choices=GENDER, default=MALE)
    result = models.CharField(max_length=80)
    created_time = models.DateField(auto_now_add=True)
