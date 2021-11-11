from rest_framework import serializers
from .models import Card, CardType


class CardSerializer(serializers.ModelSerializer):
    class Meta:
        fields = "__all__"
        model = Card


class CardTypeSerializer(serializers.ModelSerializer):
    class Meta:
        fields = "__all__"
        model = CardType
