from django.db import models

# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=50)
    age = models.IntegerField()
    image = models.ImageField(upload_to="student_image")
    college = models.CharField(max_length =100)
    address = models.TextField()

    def  __str__(self):
        return self.name
    