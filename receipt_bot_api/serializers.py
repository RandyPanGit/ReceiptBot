from rest_framework import serializers


class YourSerializer(serializers.Serializer):
    """Your data serializer, define your fields here."""
    month = serializers.CharField()
