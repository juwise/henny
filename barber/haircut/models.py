from django.db import models

class Haircut(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to="pics",blank=True, null=True)

    def __str__(self):
        return self.name

class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    number = models.CharField(max_length=50)
    comment = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name
