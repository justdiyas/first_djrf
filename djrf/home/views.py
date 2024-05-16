from rest_framework.decorators import api_view
from rest_framework.response import Response

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

