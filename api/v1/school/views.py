from rest_framework import viewsets
from .serializer import StudentSerializer
from apps.school.student.models import Student

class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer