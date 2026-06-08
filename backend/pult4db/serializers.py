from rest_framework import serializers
from .models import Company, Groups, Panel

class ListGroupsSerializer(serializers.ModelSerializer):
  class Meta:
    model = Groups
    fields = ('panel', 'group_field', 'message', 'disabled')
    
class ListCompanySerializer(serializers.ModelSerializer):
  test = serializers.SerializerMethodField()
  disabled = serializers.SerializerMethodField()
  
  def get_test(self, obj):
    return Panel.objects.get(panel_id = obj.company_id.split('#', 1)[0]).testpanel
  
  def get_disabled(self, obj):
    return Panel.objects.get(panel_id = obj.company_id.split('#', 1)[0]).disabled

  class Meta:
    model = Company
    fields = ('company_id', 'test', 'disabled', 'companyname', 'address')

class DetailCompanyMinSerializer(serializers.ModelSerializer):
  latitude = serializers.SerializerMethodField()
  longtitude = serializers.SerializerMethodField()
  operatorprompt = serializers.SerializerMethodField()

  def get_latitude(self, obj):
    return Panel.objects.get(panel_id = obj.company_id.split('#', 1)[0]).latitude
    
  def get_longtitude(self, obj):
    return Panel.objects.get(panel_id = obj.company_id.split('#', 1)[0]).longtitude

  def get_operatorprompt(self, obj):
    return Groups.objects.get(panel = obj.company_id.split('#', 1)[0], group_field = obj.company_id.split('#', 1)[1]).operatorprompt
  
  class Meta:
    model = Company
    fields = ('company_id', 'companyname', 'address', 'latitude', 'longtitude', 'operatorprompt')
  