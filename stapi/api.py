from rest_framework import viewsets
from .serializer import StudentRerializer
from .models import Students


class StudentViewSet(viewsets.ModelViewSet):
    serializer_class = StudentRerializer
    queryset = Students.objects.all()

