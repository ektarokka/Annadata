from django.db import models

# Create your models here.
class Category(models.Model):
    title=models.CharField(max_length=100)
    description=models.TextField()
    price=models.IntegerField()
    
    def _str_(self):
        return self.title
