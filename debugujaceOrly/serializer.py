from .models import Company
from rest_framework import serializers
class CompanySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Company
        fields = ['id', 'name', 'city', 'address', 'opening_hour', 'closing_hour']

