from rest_framework import generics
from .models import Company
from .serializers import ListCompanySerializer

class ListCompany(generics.ListAPIView):
    queryset = Company.objects.all().exclude(company_id__startswith = '*')
    serializer_class = ListCompanySerializer
