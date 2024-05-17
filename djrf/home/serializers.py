from rest_framework import serializers
from .models import Person, Sport

class SportSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sport
        fields = ['sport_name']

class PersonSerializer(serializers.ModelSerializer):
    sport = SportSerializer()
    class Meta:
        model = Person
        fields = '__all__'
        # depth = 1

    def validate(self, data):
        special_characters = '~`!@#$%^&*()_-+={}[]|:;"<,>.?/'
        if any(sym in special_characters for sym in data['name']):
            raise serializers.ValidationError('Name field cannot contain a special character')
        if any(sym in special_characters for sym in data['major']):
            raise serializers.ValidationError('Major field cannot contain a special character')
        if any(sym in special_characters for sym in data['city_born']):
            raise serializers.ValidationError('City born field cannot contain a special character')
        if data['age'] < 18:
            raise serializers.ValidationError('Age must be greater than 18')
        return data
