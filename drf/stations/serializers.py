from rest_framework import serializers
from stations.models import A136

class StationSerializer(serializers.ModelSerializer):
    class Meta:
        model = A136
        fields = '__all__'
