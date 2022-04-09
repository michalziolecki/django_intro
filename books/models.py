from django.db import models
from django.utils import timezone


class BookAuthor(models.Model):
    name = models.TextField()

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.TextField()

    def __str__(self):
        return self.name


class Book(models.Model):
    title = models.TextField()
    authors = models.ManyToManyField(BookAuthor)
    published_date = models.DateField(unique=False, null=True)
    categories = models.ManyToManyField(Category)
    average_rating = models.FloatField(default=0.0)

    def __str__(self):
        return f"{self.title} - {self.authors} - {self.published_date}"
