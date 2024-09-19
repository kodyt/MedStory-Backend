from rest_framework import serializers
from symptoms.models import Symptom

class SymptomSerializer(serializers.ModelSerializer):
    '''Describes how to serialize our data'''

    class Meta:
        model = Symptom
        fields = '__all__'
        