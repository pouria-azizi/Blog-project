import csv

from rest_framework import serializers
from . import models


class ProductSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Product
        fields = (
            'name',
            'description',
            'price'
        )


class LogoSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(required=True, allow_null=False, allow_blank=False, max_length=50)

    def create(self, validated_data):
        with open('/logoes_report.csv', 'w') as f:
            writer = csv.writer(f)
            writer.writerow(validated_data)
        return validated_data

    def update(self, instance, validated_data):
        pass
