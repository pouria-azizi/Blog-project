from rest_framework import serializers
from . import models


class OrderSerializer(serializers.ModelSerializer):
    """
    Serializers for store.Order
    """
    class Meta:
        model = models.Order
        fields = (
            'owner',
            'status',
        )
