from django.core.exceptions import ObjectDoesNotExist
from rest_framework.viewsets import ModelViewSet
from rest_framework import pagination

from .models import *
from .serializers import *

class ItemViewSet(ModelViewSet):
    serializer_class = ItemSerializer

    def get_queryset(self):
        items = Item.objects.all()

        name = self.request.GET.get('name', None)
        quantity = self.request.GET.get('quantity', None)
        quantity_gt = self.request.GET.get('quantity_gt', None)
        quantity_gte = self.request.GET.get('quantity_gte', None)
        quantity_lt = self.request.GET.get('quantity_lt', None)
        quantity_lte = self.request.GET.get('quantity_lte', None)

        try:
            if name:
                items = items.filter(name__icontains=name)
            if quantity:
                items = items.filter(quantity=int(quantity))
            if quantity_gt:
                items = items.filter(quantity__gt=int(quantity_gt))
            if quantity_gte:
                items = items.filter(quantity__gte=int(quantity_gte))
            if quantity_lt:
                items = items.filter(quantity__lt=int(quantity_lt))
            if quantity_lte:
                items = items.filter(quantity__lte=int(quantity_lte))
        except ValueError:
            items = Item.objects.none()

        return items

class EventViewSet(ModelViewSet):
    serializer_class = EventSerializer

    def get_queryset(self):
        events = Event.objects.all()

        item = self.request.GET.get('item', None)
        year = self.request.GET.get('year', None)
        month = self.request.GET.get('month', None)

        try:
            if item:
                events = Item.objects.get(pk=int(item)).events.all()
            if year:
                events = events.filter(timestamp__year=int(year))
            if month:
                events = events.filter(timestamp__month=int(month))
        except (ValueError, ObjectDoesNotExist):
            events = Event.objects.none()

        return events
