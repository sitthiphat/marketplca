from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from .models import Seller,Buyer


@receiver(post_save, sender=User)
def create_seller(sender, instance, created, **kwargs):
    if created:
        Seller.objects.create(user=instance)
        
        
@receiver(post_save, sender=User)
def create_buyer(sender, instance, created, **kwargs):
    if created:
        Buyer.objects.create(user=instance)



@receiver(post_save, sender=User)
def save_seller(sender, instance, **kwargs):
    instance.seller.save()
    
@receiver(post_save, sender=User)
def save_buyer(sender, instance, **kwargs):
    instance.buyer.save()
