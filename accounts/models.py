from django.db import models
from django.contrib.auth import get_user_model
# Create your models here.
model = get_user_model()
class connection(models.Model):
    user = models.ForeignKey(model,on_delete=models.CASCADE,related_name='user')
    connections = models.ManyToManyField(model,related_name='connections')

    def __str__(self):
        return self.user.username