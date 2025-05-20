from django.db import models

# Create your models here.

class Author(models.Model):
    name = models.CharField(max_length=50)
    bio = models.TextField(null=False, blank=True)

    def __str__(self):
        return super().__str__()

class Post (models.Model):
    title = models.CharField(max_length=50)
    content = models.TextField()
    published_date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)

    def __str__(self):
        return super().__str__()
