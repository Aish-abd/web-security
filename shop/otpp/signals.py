from main.models import User_Custom
from .models import Code
from django.db.models.signals import post_save
from django.dispatch import receiver

@receiver(post_save,sender=User_Custom)
def code_generate_save(sender,instance,created,*args,**kwargs):
    if created:
        Code.objects.create(user=instance)