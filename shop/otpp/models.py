from django.db import models
import random
from main.models import User_Custom
# Create your models here.
class Code(models.Model):
    #field to store user's code
    number=models.CharField(max_length=5,blank=True)
    #match code to user
    user=models.OneToOneField(User_Custom,on_delete=models.CASCADE)
    #return the 5-digit code as a string
    def __str__(self):
        return str(self.number)
    #generate a random 5-digit
    def save(self,*args,**kwargs):
        number_list=[0,1,2,3,4,5,6,7,8,9]
        cd_items=[]
        for i in range(5):
              num=random.choice(number_list)
              cd_items.append(num)

        cd_str="".join(str(item) for item in cd_items)
        self.number=cd_str
        super().save(*args,**kwargs)