from rest_framework import serializers
from .models import Person


class PersonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Person
        fields = '__all__'

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
