from .models import Company
from rest_framework import viewsets
from .serializer import CompanySerializer
class CompanyViewSet(viewsets.ModelViewSet):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer

