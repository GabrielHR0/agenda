from django.db import models
from django.utils import timezone

class Contact(models.Model):
    firstName = models.CharField(max_length=50)
    lastName = models.CharField(max_length=50, blank=True)
    phone = models.CharField(max_length=50)
    email = models.EmailField(max_length=255, blank=True)
    createdDate = models.DateTimeField(default=timezone.now)
    descripition = models.TextField(blank=True)
    show = models.BooleanField(default=True)
    picture = models.ImageField(blank=True, upload_to='pictures/%Y/%M/')

    def __str__(self) -> str:
        return f'{self.firstName} {self.lastName}'
    
