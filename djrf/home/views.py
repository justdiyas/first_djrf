from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Person
from .serializers import PersonSerializer
from django.shortcuts import get_object_or_404

@api_view(['GET', 'POST', 'PUT', 'DELETE'])
def index(request):
    courses = {
        'course_name': 'Python Backend Development',
        'course_difficulty': 'Easy to Medium',
        'course_subjects': ['Python Fundamentals', 'Django', ' Django RestFrameWork', 'SQL basics']
    }
    if request.method == 'GET':
        print('You get the data via GET request')
        return Response(courses)
    elif request.method == 'POST':
        data = request.data
        print('You updated the data via POST request')
        print(data)
        return Response(courses)
    elif request.method == 'PUT':
        print('You modified the data via PUT request')
        return Response(courses)
    elif request.method == 'DELETE':
        print('You deleted the data via DELETE request')
        return Response(courses)


@api_view(['GET', 'POST'])
def person(request):
    if request.method == 'GET':
        person = Person.objects.all()
        serializer = PersonSerializer(person, many=True)
        return Response(serializer.data)
    else:
        data = request.data
        serializer = PersonSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)
