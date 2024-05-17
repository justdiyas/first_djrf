from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Person
from .serializers import PersonSerializer
from django.shortcuts import get_object_or_404


@api_view(['GET', 'POST', 'PUT', 'PATCH'])
def person(request):
    if request.method == 'GET':
        person = Person.objects.filter(sport__isnull=False)
        serializer = PersonSerializer(person, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        data = request.data
        serializer = PersonSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)
    elif request.method == 'PUT':
        data = request.data
        person = Person.objects.get(id=data.get('id'))
        serializer = PersonSerializer(person, data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)
    else:
        data = request.data
        person = Person.objects.get(name=data.get('name'))
        serializer = PersonSerializer(person, data=data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)


@api_view(['GET', 'DELETE'])
def person_delete(request, person_id):
    person = get_object_or_404(Person, id=person_id)
    if request.method == 'GET':
        serializer = PersonSerializer(person)
        return Response(serializer.data)
    else:
        person.delete()
        return Response(f'{person} has been deleted!')