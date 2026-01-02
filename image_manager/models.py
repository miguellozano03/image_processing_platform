from django.db import models
from accounts.models import User

class Image(models.Model):
    owner = models.ForeignKey(User,on_delete=models.CASCADE)
    file = models.ImageField(upload_to='images/originals')
    created_at = models.DateTimeField(auto_now_add=True)