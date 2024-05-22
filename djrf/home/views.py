from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import viewsets
from rest_framework import status
from .models import Person
from .serializers import PersonSerializer, LoginSerializer, RegisterUser
from django.shortcuts import get_object_or_404


class UserRegisterAPI(APIView):
    def post(self, request):
        serializer = RegisterUser(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response('User successfully created!')
        return Response(serializer.errors)



@api_view(['GET', 'POST', 'PUT', 'PATCH'])
def person(request):
    if request.method == 'GET':
        person = Person.objects.all()
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


@api_view(['POST'])
def login(request):
    data = request.data
    serializer = LoginSerializer(data=data)
    if serializer.is_valid():
        data = serializer.validated_data
        return Response('Success!')
    return Response(serializer.errors)


class PersonAPI(APIView):
    def get(self, request):
        person = Person.objects.all()
        serializer = PersonSerializer(person, many=True)
        return Response(serializer.data)

    def post(self, request):
        data = request.data
        serializer = PersonSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

    def put(self, request):
        data = request.data
        person = Person.objects.get(id=data.get('id'))
        serializer = PersonSerializer(person, data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

    def patch(self, request):
        data = request.data
        person = Person.objecs.get(id=data.get('id'))
        serializer = PersonSerializer(person, data=data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)


class PersonDeleteAPI(APIView):
    def get(self, request, id):
        person = get_object_or_404(Person, id=id)
        serializer = PersonSerializer(person)
        return Response(serializer.data)

    def delete(self, request, id):
        person = get_object_or_404(Person, id=id)
        person.delete()
        return Response(f'Data on {person} has been deleted from database.', status=status.HTTP_202_ACCEPTED)


class PersonViewSetAPI(viewsets.ModelViewSet):
    serializer_class = PersonSerializer
    queryset = Person.objects.all()

    def list(self, request):
        search = request.GET.get('search')
        queryset = self.queryset
        if search:
            queryset = queryset.filter(name__startswith=search)
        serializer = PersonSerializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


