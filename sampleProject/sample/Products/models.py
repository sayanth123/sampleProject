from django.db import models

# Create your models here.
class Product(models.Model):
    name=models.CharField(max_length=250)
    weight=models.IntegerField()
    price=models.FloatField()
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name