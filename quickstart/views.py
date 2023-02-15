from django.shortcuts import render
from quickstart.models import Student
from rest_framework.views import APIView
from rest_framework.response import Response

# Create your views here.
class StudentView(APIView):
    def get(self, request):
        lst = Student.objects.all().values()
        return Response({'student': list(lst)})