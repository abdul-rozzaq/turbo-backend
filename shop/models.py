from django.db import models



class Shop(models.Model):
    name = models.CharField(max_length=256)
    password = models.CharField(max_length=256)
    
    def __str__(self) -> str:
        return self.name
    
    