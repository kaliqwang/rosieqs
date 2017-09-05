from django.db import models
from django.db.models import Sum
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from django.utils import timezone

class Item(models.Model):
    name = models.CharField(max_length=100, blank=True)
    quantity = models.PositiveIntegerField(editable=False)
    initial_quantity = models.PositiveIntegerField()

    def __str__(self):
        return str(self.pk) + '.' + self.name

    def save(self, *args, **kwargs):
        if self.pk is None:
            self.quantity = self.initial_quantity
        super(Item, self).save(*args, **kwargs)

class Event(models.Model):
    item = models.ForeignKey(Item, related_name='events', on_delete=models.CASCADE)
    quantity_change = models.IntegerField()
    timestamp = models.DateTimeField(editable=False, default=timezone.now)

@receiver([post_save, post_delete], sender=Event)
def update_item_quantity(sender, **kwargs):
    item = kwargs["instance"].item
    if item: # if item exists (wasn't deleted), update item quantity information
        net_quantity_change = item.events.all().aggregate(Sum('quantity_change'))['quantity_change__sum']
        if net_quantity_change is None:
            net_quantity_change = 0
        item.quantity = item.initial_quantity + net_quantity_change
        item.save()
