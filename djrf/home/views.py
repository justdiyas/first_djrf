from rest_framework.decorators import api_view
from rest_framework.response import Response

@api_view(['GET', 'POST'])
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
        print('You get the data  via POST request')
        return Response(courses) 
