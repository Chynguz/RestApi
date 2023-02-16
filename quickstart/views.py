# from django.shortcuts import render
from quickstart.models import Student
# from rest_framework.views import APIView
from rest_framework.response import Response
# from django.forms import model_to_dict
from rest_framework import generics
from .serializer import StudentSerializer

# Create your views here.
# class StudentView(APIView):
#     def get(self, request):
#         lst = Student.objects.all().values()
#         return Response({'student': list(lst)})
    
#     def post(self, request):
#         lst = Student.objects.create(
#             first_name = request.data['first_name'],
#             last_name = request.data['last_name'],
#             age = request.data['age'],
#             gender = request.data['gender'],
#         )
#         return Response('Created')


class StudentListView(generics.ListAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

class StudentCreateView(generics.CreateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer


class StudentDeleteView(generics.DestroyAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

class StudentUpdateView(generics.UpdateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

class StudentRetriveView(generics.RetrieveAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    