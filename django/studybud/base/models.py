from audioop import reverse
from datetime import datetime
from django.db import models

# Create your models here.

class Student(models.Model):
    roll_no = models.TextField()
    name = models.TextField(max_length = 40)
    email = models.EmailField(default='site@site.com')
    stud_class = models.TextField()
    department = models.TextField()
    photo = models.ImageField(null=True)
    documents = models.FileField(null=True)
    created_at = models.DateField(auto_now=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('model-detail-view', args=[str(self.id)])


class Questions(models.Model):
    name  = models.TextField()
    description = models.TextField()
    status=models.TextField()
