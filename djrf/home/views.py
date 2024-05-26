from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework import viewsets, status, generics
from .models import Person, Sport
from .serializers import PersonSerializer, LoginSerializer, RegisterUser, SportSerializer
from django.shortcuts import get_object_or_404
from django.http import Http404


@api_view(['GET', 'POST', 'PUT', 'PATCH'])
@permission_classes([IsAuthenticated, IsAdminUser])
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
@permission_classes([IsAuthenticated, IsAdminUser])
def person_delete(request, person_id):
    person = get_object_or_404(Person, id=person_id)
    if request.method == 'GET':
        serializer = PersonSerializer(person)
        return Response(serializer.data)
    else:
        person.delete()
        return Response(f'{person} has been deleted!')


class PersonAPI(APIView):
    permission_classes = [IsAuthenticated, IsAdminUser]

    def get(self, request):
        person = Person.objects.all()
        serializer = PersonSerializer(person, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = PersonSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Responses(serializer.data)
        return Response(serializer.errors)


class PersonDetailAPI(APIView):
    permission_classes = [IsAuthenticated, IsAdminUser]

    def get_object(self, pk):
        try:
            person = Person.objects.get(id=pk)
            return person
        except Person.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        person = self.get_object(pk)
        serializer = PersonSerializer(person)
        return Response(serializer.data)

    def put(self, request, pk):
        # person = Person.objects.get(id=request.data.get('id'))
        person = self.get_object(pk)
        serializer = PersonSerializer(person, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

    def patch(self, request, pk):
        # person = Person.objects.get(id=request.data.get('id'))
        person = self.get_object(pk)
        serializer = PersonSerializer(person, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

    def delete(self, request, pk):
        # person = get_object_or_404(Person, id=id)
        person = self.get_object(pk)
        person.delete()
        return Response(f'Data on {person} has been deleted from database.', status=status.HTTP_202_ACCEPTED)


class PersonViewSetAPI(viewsets.ModelViewSet):
    serializer_class = PersonSerializer
    queryset = Person.objects.all()
    permission_classes = [IsAuthenticated, IsAdminUser]

    # def list(self, request):
    #     search = request.GET.get('search')
    #     queryset = self.queryset
    #     if search:
    #         queryset = queryset.filter(name__startswith=search)
    #     serializer = PersonSerializer(queryset, many=True)
    #     return Response(serializer.data, status=status.HTTP_200_OK)


class UserRegisterAPI(APIView):
    def post(self, request):
        serializer = RegisterUser(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response('User successfully created!')
        return Response(serializer.errors)


class UserLoginAPI(APIView):
    def post(self, request):
        serializer = LoginSerializer(data=request.data)
        if serializer.is_valid():
            return Response(f'{request.user} is logged in')
        return Response(serializer.errors)


class SportListAPI(viewsets.ModelViewSet):
    queryset = Sport.objects.all()
    serializer_class = SportSerializer
    permission_classes = [IsAuthenticated, IsAdminUser]


