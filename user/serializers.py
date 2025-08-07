from rest_framework import serializers
from .models import Profile, Dossier

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        exclude = ['email']

class DossierSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dossier
        exclude = ['id','owner']

