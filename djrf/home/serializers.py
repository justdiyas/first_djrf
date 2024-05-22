from rest_framework import serializers
from .models import Person, Sport
from django.contrib.auth.models import User

class RegisterUser(serializers.Serializer):
    username = serializers.CharField()
    email = serializers.EmailField()
    password = serializers.CharField()

    def validate(self, data):
        if data['username']:
            if User.objects.filter(username=data['username']).exists():
                raise serializers.ValidationError('Given username already exists')
        if data['email']:
            if User.objects.filter(email=data['email']).exists():
                raise serializers.ValidationError('Given email already exists')
        return data

    def create(self, validated_data):
        user = User.objects.create(**validated_data)
        user.set_password(validated_data.get('password'))
        user.save()
        return user


class SportSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sport
        fields = ['sport_name']


class PersonSerializer(serializers.ModelSerializer):
    sport = SportSerializer()
    country = serializers.SerializerMethodField()

    class Meta:
        model = Person
        fields = '__all__'
        # depth = 1

    def get_country(self, obj):
        return 'Kazakhstan'

    def validate(self, data):
        special_characters = '~`!@#$%^&*()+={}[]|:;"<,>?/'
        if any(sym in special_characters for sym in data['name']):
            raise serializers.ValidationError('Name field cannot contain a special character')
        if any(sym in special_characters for sym in data['major']):
            raise serializers.ValidationError('Major field cannot contain a special character')
        if any(sym in special_characters for sym in data['city_born']):
            raise serializers.ValidationError('City born field cannot contain a special character')
        if data['age'] < 18:
            raise serializers.ValidationError('Age must be greater than 18')
        return data

    def create(self, validated_data):
        sport_data = validated_data.pop('sport')
        sport = Sport.objects.get(**sport_data)
        person = Person.objects.create(sport=sport, **validated_data)
        return person

    def update(self, instance, validated_data):
        sport_data = validated_data.pop('sport')
        sport = Sport.objects.get(**sport_data)
        instance.name = validated_data.get('name')
        instance.age = validated_data.get('age')
        instance.major = validated_data.get('major')
        instance.city_born = validated_data.get('city_born')
        instance.sport = sport
        instance.save()
        return instance


class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()

