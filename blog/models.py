from django.db import models
from time import timezone
from home.models import Category
from django.contrib.auth.models import User

# Create your models here.

# class Article(models.Model):
#     author = models.ForeignKey(User, on_delete=models.CASCADE)
#     title = models.CharField(max_length=90)
#     category = models.ManyToManyField(Category)
#     description = models.TextField()
#     image = models.ImageField(upload_to="articles/images")
    

#     def __str__(self):
#         return self.title

class Article(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.ManyToManyField(Category)
    title = models.CharField(max_length=30)
    sub_title = models.CharField(max_length=60)
    description = models.TextField()
    image = models.ImageField(upload_to="blog_picturr")
    sub_image = models.ImageField(upload_to="blog_picture")
    create_date = models.DateTimeField(default=timezone)


   

    def __str__(self):
        return f'{self.title} - {self.sub_title}'

    class Meta:
        verbose_name = "مقاله"
        verbose_name_plural = "مقالات"



class Comment(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name='comments')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comments')
    parent = models.ForeignKey('self', null=True, blank=True, on_delete=models.CASCADE, related_name="replies")
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.body[:50]

    
    class Meta:
        verbose_name = "نظر"
        verbose_name_plural = "نظریات"