from django.shortcuts import render

from rest_framework import generics
from .models import Company
from .serializers import ListCompanySerializer, DetailCompanyMinSerializer

class ListCompany(generics.ListAPIView):
  queryset = Company.objects.all().exclude(company_id__startswith = '*')
  serializer_class = ListCompanySerializer

class DetailCompany(generics.RetrieveAPIView):
  queryset = Company.objects.all().exclude(company_id__startswith = '*')
  serializer_class = DetailCompanyMinSerializer
  lookup_field = 'company_id'

  def get_object(self):
    return Company.objects.get(company_id=self.kwargs['company_id'].replace('&','#'))

