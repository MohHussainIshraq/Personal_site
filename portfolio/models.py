from django.db import models
from home.models import Category
# Create your models here.

class Portfolio_Info(models.Model):
    category = models.ManyToManyField(Category)
    client = models.CharField(max_length=50)
    project_date = models.DateTimeField(auto_now_add=True)
    web_address = models.URLField()
    title = models.CharField(max_length=42)
    description = models.TextField()
    image = models.ImageField()

    def __str__(self):
        return f"{self.title} - {self.description[:30]}"


    class Meta:
        verbose_name = "نمونه فعالیت"
        verbose_name_plural = "نمونه فعالیت ها"


class Images(models.Model):
    image1 = models.ImageField()
    image2 = models.ImageField()
    image3 = models.ImageField()


    class Meta:
        verbose_name = "تصویر"
        verbose_name_plural = "تصاویر"

