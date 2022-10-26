from django.dispatch import receiver
from django.db.models.signals import pre_save
from .models import BookModel


@receiver(pre_save, sender=BookModel)
def real_price(sender, instance, **kwargs):
    if instance.is_discount:
        instance.real_price = instance.price - instance.price * (instance.discount / 100)
        return instance.real_price
    else:
        instance.real_price = instance.price
        return instance.real_price
