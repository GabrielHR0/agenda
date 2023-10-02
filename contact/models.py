from django.db import models
from django.utils import timezone

class Category(models.Model):
    name = models.CharField(max_length=50)

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

    def __str__(self) -> str:
        return f'{self.name}'

class Contact(models.Model):
    firstName = models.CharField(max_length=50)
    lastName = models.CharField(max_length=50, blank=True)
    phone = models.CharField(max_length=50)
    email = models.EmailField(max_length=255, blank=True)
    createdDate = models.DateTimeField(default=timezone.now)
    descripition = models.TextField(blank=True)
    show = models.BooleanField(default=True)
    picture = models.ImageField(blank=True, upload_to='pictures/%Y/%M/')
    category = models.ForeignKey(Category, 
        on_delete = models.SET_NULL,  
        blank = True,
        null = True,
        )
    
    def __str__(self) -> str:
        return f'{self.firstName} {self.lastName}'