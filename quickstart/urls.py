from django.urls import path
from quickstart.views import StudentView

urlpatterns = [
    path('api/', StudentView.as_view())
]
