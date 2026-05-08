from rest_framework import serializers
from .models import Company, Panel

class ListCompanySerializer(serializers.ModelSerializer):
  panel = serializers.SerializerMethodField()
  test = serializers.SerializerMethodField()
  disabled = serializers.SerializerMethodField()

  def get_panel(self, obj):
     return obj.company_id.split('#', 1)[0]
  
  def get_test(self, obj):
     return Panel.objects.get(panel_id = obj.company_id.split('#', 1)[0]).testpanel
  
  def get_disabled(self, obj):
     return Panel.objects.get(panel_id = obj.company_id.split('#', 1)[0]).disabled

  class Meta:
      model = Company
      fields = ('panel', 'test', 'disabled', 'companyname', 'address')
