from django.db import models

# Create your models here.

class Number(models.Model):
    Number = models.IntegerField()
    
def __str__(self):
    return f"{self.Number} + 'this is your input'"

