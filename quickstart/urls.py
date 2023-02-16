from django.urls import path
from quickstart.views import StudentListView, StudentCreateView, StudentRetriveView, StudentUpdateView, StudentDeleteView

urlpatterns = [
    path('api/', StudentListView.as_view()),
    path('create/', StudentCreateView.as_view()),
    path('retrive/<int:pk>', StudentRetriveView.as_view()),
    path('update/<int:pk>', StudentUpdateView.as_view()),
    path('delete/<int:pk>', StudentDeleteView.as_view()),
]
