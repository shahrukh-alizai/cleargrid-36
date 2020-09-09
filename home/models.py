from django.conf import settings
from django.db import models

# Create your models here.

from django.db import models


class CustomText(models.Model):
    title = models.CharField(
        max_length=150,
    )

    def __str__(self):
        return self.title

    @property
    def api(self):
        return f"/api/v1/customtext/{self.id}/"

    @property
    def field(self):
        return "title"


class HomePage(models.Model):
    body = models.TextField()

    @property
    def api(self):
        return f"/api/v1/homepage/{self.id}/"

    @property
    def field(self):
        return "body"


class Demo(models.Model):
    "Generated Model"
    name = models.CharField(
        max_length=256,
    )


class Student(models.Model):
    "Generated Model"
    tests = models.CharField(
        max_length=256,
    )


class Books(models.Model):
    "Generated Model"
    user2 = models.CharField(
        max_length=256,
    )


class Test(models.Model):
    "Generated Model"
    newapp = models.BigIntegerField()


class NewApp(models.Model):
    "Generated Model"
    user2 = models.BigIntegerField()

    class Meta:
        verbose_name_plural = "NewApp"


class NewApp(models.Model):
    "Generated Model"
    user2 = models.BigIntegerField()

    class Meta:
        verbose_name_plural = "NewApp"
