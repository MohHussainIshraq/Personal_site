from time import timezone
from django.db import models

# Create your models here.

class Services(models.Model):
    title = models.CharField(max_length=40)
    description = models.TextField()
    image = models.ImageField(upload_to="services")


    def __str__(self):
        return self.title


class Sub_title(models.Model):
    sub_title = models.CharField(max_length=100)


    def __str__(self):
        return self.sub_title[:14]


class About(models.Model):
    title = models.CharField(max_length=30)
    description = models.TextField()
    name = models.CharField(max_length=30)
    profile = models.CharField(max_length=50)
    email = models.EmailField()
    phone = models.CharField(max_length=15)

    
    def __str__(self):
        return self.title


class Category(models.Model):
    title = models.CharField(max_length=40)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class Portfolio(models.Model):
    title = models.CharField(max_length=30)
    category = models.ManyToManyField(Category)
    image = models.ImageField(upload_to="portfolio")
    created = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.title

class Skill(models.Model):
    name_skill = models.CharField(max_length=25)
    percent_skill = models.CharField(max_length=4)


    def __str__(self):
        return self.name_skill



class Contact_us(models.Model):
    title = models.CharField(max_length=35)
    description = models.TextField()
    address = models.CharField(max_length=100)
    phone = models.CharField(max_length=12)
    email = models.EmailField()

    facebook = models.CharField(max_length=55)
    instagram = models.CharField(max_length=60)
    twitter = models.CharField(max_length=45)
    linkedin = models.CharField(max_length=50)


    def __str__(self):
        return self.title


class Message(models.Model):
    name = models.CharField(max_length=30)
    email = models.EmailField(max_length=50)
    subject = models.CharField(max_length=45)
    message = models.TextField()


    def __str__(self):
        return f"{self.name} - {self.email}"


class Blog(models.Model):
    title = models.CharField(max_length=30)
    sub_title = models.CharField(max_length=60)
    description = models.TextField()
    image = models.ImageField(upload_to="blog_picturr")
    sub_image = models.ImageField(upload_to="blog_picture")
    author = models.CharField(max_length=38)
    create_date = models.DateTimeField(default=timezone)


    def __str__(self):
        return f'{self.title} - {self.sub_title}'


class Footer(models.Model):
    fname = models.CharField(max_length=38)
    lname = models.CharField(max_length=36)


    def __str__(self):
        return f"{self.fname} - {self.lname}"


class Counters(models.Model):
    works_completed = models.IntegerField(null=True)
    years_experience = models.IntegerField(null=True)
    total_clients = models.IntegerField(null=True)
    award_won = models.IntegerField(null=True)
    

class Testimonial(models.Model):
    author1 = models.CharField(max_length=42)
    description1 = models.TextField()
    author2 = models.CharField(max_length=20)
    description2 = models.TextField()

    def __str__(self):
        return f"{self.author1} - {self.description1[:30]} & {self.author2} - {self.description2[:30]}"
