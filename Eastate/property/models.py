from django.db import models
from django.contrib.auth.models import User

# Create your models here.


# Team
class Team(models.Model):
    imageSrc = models.ImageField(upload_to="media/static/images/")
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=250)
    phone = models.CharField(max_length=12)
    email = models.EmailField(max_length=250)

    def __str__(self):
        return self.title


# Property
class Property(models.Model):
    CATEGORY_CHOICES = (
        ("For Sale", "For Sale"),
        ("For Rent", "For Rent"),
    )

    image = models.ImageField(upload_to="media/static/images/")
    title = models.CharField(max_length=250)
    description = models.CharField(max_length=1000, default="")
    location = models.CharField(max_length=250, default="")
    type = models.CharField(max_length=100, default="")
    price = models.CharField(max_length=100)
    area = models.CharField(max_length=50)
    beds = models.CharField(max_length=10)
    baths = models.CharField(max_length=5)
    garages = models.CharField(max_length=5)
    category = models.CharField(
        max_length=20, choices=CATEGORY_CHOICES, default="For Sale"
    )

    def __str__(self):
        return self.title


# News
class News(models.Model):
    CATEGORY_CHOICES = (
        ("Travel", "Travel"),
        ("Picnic", "Picnic"),
    )
    imageSrc = models.ImageField(upload_to="media/static/images/")
    author = models.CharField(max_length=50, default="")
    description = models.TextField(max_length=2000, default="")
    quote = models.TextField(max_length=250, default="")
    paragraphShort = models.TextField(max_length=250, default="")
    paragraphLong = models.TextField(max_length=250, default="")
    paragraph = models.TextField(max_length=250, default="")
    title = models.CharField(max_length=25)
    date = models.DateField(auto_now_add=True)
    category = models.CharField(
        max_length=20, choices=CATEGORY_CHOICES, default="Travel"
    )

    def __str__(self):
        return self.title


# About
class About(models.Model):
    about = models.CharField(max_length=500)
    email = models.EmailField(max_length=250)
    phone = models.CharField(max_length=20)
    address = models.CharField(max_length=500)

    def __str__(self):
        return self.email


# Agent
class Agent(models.Model):
    imageSrc = models.ImageField(upload_to="media/static/images/")
    title = models.CharField(max_length=250)
    description = models.CharField(max_length=250)
    phone = models.CharField(max_length=30)
    email = models.EmailField(max_length=250)

    def __str__(self):
        return self.title


# Message
class Messages(models.Model):
    name = models.CharField(max_length=250)
    email = models.EmailField(max_length=250)
    comment = models.TextField(max_length=500)

    def __str__(self):
        return self.name


class ContactUs(models.Model):
    name = models.CharField(max_length=250)
    email = models.EmailField(max_length=250)
    comment = models.TextField(max_length=500)

    def __str__(self):
        return self.name
