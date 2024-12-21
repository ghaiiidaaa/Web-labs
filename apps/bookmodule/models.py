from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=200, null=True, blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    edition = models.IntegerField()

    def __str__(self):
        return self.title


class Address(models.Model):
    city = models.CharField(max_length=100)

    def __str__(self):
        return self.city

class Student(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    address = models.ForeignKey(Address, on_delete=models.CASCADE)

    def __str__(self):
        return self.name



class Address2(models.Model):  # Renamed to avoid conflicts with the previous Address model
    city = models.CharField(max_length=100)

    def __str__(self):
        return self.city

class Student2(models.Model):  # Renamed to avoid conflicts with the previous Student model
    name = models.CharField(max_length=100)
    age = models.PositiveIntegerField()
    addresses = models.ManyToManyField(Address2)  # Many-to-many relationship

    def __str__(self):
        return self.name
    
class ImageModel(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='images/')  # Images should be saved to 'media/images/'

    def __str__(self):
        return self.title

# Create your models here.