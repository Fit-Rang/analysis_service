from rest_framework import serializers

class VerdictDetailSerializer(serializers.Serializer):
    analysis = serializers.CharField()
    score = serializers.IntegerField()
    details = serializers.CharField()

class VerdictResponseSerializer(serializers.Serializer):
    verdict = VerdictDetailSerializer()
