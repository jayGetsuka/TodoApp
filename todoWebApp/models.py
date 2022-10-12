from django.db import models

# Create your models here.
class Todo(models.Model):
    title = models.CharField(max_length=500)
    description = models.TextField()
    deadline = models.DateTimeField()
    done = models.BooleanField(default=False)
