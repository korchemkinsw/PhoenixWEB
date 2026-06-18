from django.shortcuts import render

from rest_framework import generics
from .models import Company, Groupresponse, Groups
from .serializers import ListCompanySerializer, DetailCompanyMinSerializer, ListGroupsSerializer, ListGroupResponseSerializer

class ListGroupResponse(generics.ListAPIView):
  serializer_class = ListGroupResponseSerializer

  def get_queryset(self):
    return Groupresponse.objects.using('pult4db').filter(description__startswith = 'ГБР')

class ListGroups(generics.ListAPIView):
  serializer_class = ListGroupsSerializer

  def get_queryset(self):
    return Groups.objects.using('pult4db').filter(panel=self.kwargs['company_id'].split('&', 1)[0])

class ListCompany(generics.ListAPIView):
  queryset = Company.objects.using('pult4db').all().exclude(company_id__startswith = '*')
  serializer_class = ListCompanySerializer

class DetailCompany(generics.RetrieveAPIView):
  queryset = Company.objects.using('pult4db').all().exclude(company_id__startswith = '*')
  serializer_class = DetailCompanyMinSerializer
  lookup_field = 'company_id'

  def get_object(self):
    print(self.kwargs)
    return Company.objects.using('pult4db').get(company_id=self.kwargs['company_id'].replace('&','#'))
