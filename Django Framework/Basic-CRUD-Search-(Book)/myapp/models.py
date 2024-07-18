from django.db import models
from django.utils import timezone

# Create your models here.

class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def save(self,*args,**kwargs):
        if self.pk:
            self.updated_at = timezone.now()
        self.created_at = timezone.now()

        super(BaseModel,self).save(*args,**kwargs)


class Book(BaseModel):
    title = models.CharField(max_length=255)
    autor = models.CharField(max_length=255)

    def __str__(self):
        return self.title + " by " + f'\"{self.autor}\"'
    
        