from django.db import models

# Create your models here.
    
class toDo(models.Model):
    title = models.CharField(max_length=30)
    create_at = models.DateTimeField()

    def __str__(self):
        return self.title