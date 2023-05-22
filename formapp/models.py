from django.db import models

# Create your models here.

class Number(models.Model):
    first_number = models.CharField( max_length=50)
    
def __str__(self):
    return f"{self.first_number} + 'this is your input'"
