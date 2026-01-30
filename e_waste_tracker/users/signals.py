from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import CustomUser

@receiver(post_save, sender=CustomUser)
def create_warehouse(sender, instance, created, **kwargs):
    if created:
        from warehouse.models import Warehouse
        Warehouse.objects.create(
            owner=instance,
            manager=instance,
            name=f"{instance.username}'s Warehouse"
        )