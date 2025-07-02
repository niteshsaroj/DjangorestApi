from rest_framework import serializers
from .models import Country,States

class CountrySerializer(serializers.ModelSerializer):
    class Meta:
        model=Country
        fields=['id','name','capital','area']
        
class StateSerializer(serializers.ModelSerializer):
    country=CountrySerializer(read_only=True)
    country_id=serializers.PrimaryKeyRelatedField(
        queryset=Country.objects.all(),write_only=True)

    class Meta:
        model=States
        fields=['id','name','country','country_id']
    
    def create(self,validated_data):
        country=validated_data.pop('country_id')
        return States.objects.create(country=country,**validated_data)
    
    def update(self,instance,validated_data,):
        if 'country_id' in validated_data:
            instance.country=validated_data.pop('country_id')
        instance.name=validated_data.get('name',instance.name)
        instance.save()
        return instance