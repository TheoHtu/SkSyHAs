from django.db import models

# Create your models here.
class TODO(models.Model):
    name = models.CharField(max_length=160)
    deadline = models.DateTimeField()
    fortschritt = models.IntegerField(default=0)
    def __str__(self):
        return self.name