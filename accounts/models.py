from django.db import models
from django.contrib.auth import get_user_model
from django.db.models import Q
from channels.db import SyncToAsync
# Create your models here.
model = get_user_model()
class connection(models.Model):
    user = models.ForeignKey(model,on_delete=models.CASCADE,related_name='user')
    connections = models.ManyToManyField(model,related_name='connections')

    def __str__(self):
        return self.user.username





class threadmanager(models.Manager):
    
    
    def get_thread(self,firstuser,seconduser):

        
        try :
            thread = self.get_queryset().get(first=firstuser,second=seconduser)
            print("1",thread)
            
        
        except :
            try:
                thread = self.get_queryset().get(first=seconduser,second=firstuser)
                print("2",thread)
            except:
                thread = self.model(first=firstuser,second=seconduser)
                thread.save()  
          
        
        return thread


class thread(models.Model):

    first = models.ForeignKey(model,on_delete=models.CASCADE,related_name="first")
    second = models.ForeignKey(model,on_delete=models.CASCADE,related_name="second")


    objects = threadmanager()   
    
    def __str__(self):
        return self.first.username + "-" + self.second.username
    