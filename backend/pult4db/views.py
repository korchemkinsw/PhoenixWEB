from django.shortcuts import render

from rest_framework import generics
from .models import Company, Groups
from .serializers import ListCompanySerializer, DetailCompanyMinSerializer, ListGroupsSerializer

class ListGroups(generics.ListAPIView):
  serializer_class = ListGroupsSerializer

  def get_queryset(self):
    return Groups.objects.filter(panel=self.kwargs['company_id'].split('&', 1)[0])

class ListCompany(generics.ListAPIView):
  queryset = Company.objects.all().exclude(company_id__startswith = '*')
  serializer_class = ListCompanySerializer

class DetailCompany(generics.RetrieveAPIView):
  queryset = Company.objects.all().exclude(company_id__startswith = '*')
  serializer_class = DetailCompanyMinSerializer
  lookup_field = 'company_id'

  def get_object(self):
    return Company.objects.get(company_id=self.kwargs['company_id'].replace('&','#'))

