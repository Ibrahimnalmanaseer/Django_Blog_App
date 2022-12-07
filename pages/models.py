from django.db import models
from accounts.models import CustomUser
from datetime import datetime
from django.urls import reverse

# Create your models here.

class Blog(models.Model):

    title=models.CharField(max_length=50,null=False)
    body=models.TextField()
    author=models.ForeignKey(CustomUser,on_delete=models.CASCADE)
    date=models.DateField(default=datetime.now, blank=True)
    image=models.URLField(null=True)

    def __str__(self) -> str:
        return self.title
    def get_absolute_url(self):

        return reverse('home')



