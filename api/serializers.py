from rest_framework import serializers

from .models import *

class ItemSerializer(serializers.HyperlinkedModelSerializer):
    initial_quantity = serializers.IntegerField(min_value=0)

    def __init__(self, *args, **kwargs):
        many = kwargs.pop('many', True)
        super(ItemSerializer, self).__init__(many=many, *args, **kwargs)

    class Meta:
        model = Item
        fields = ('id', 'name', 'quantity', 'initial_quantity')

class EventSerializer(serializers.HyperlinkedModelSerializer):
    item = serializers.PrimaryKeyRelatedField(queryset=Item.objects.all())

    def __init__(self, *args, **kwargs):
        many = kwargs.pop('many', True)
        super(EventSerializer, self).__init__(many=many, *args, **kwargs)

    class Meta:
        model = Event
        fields = ('id', 'item', 'quantity_change', 'timestamp')
