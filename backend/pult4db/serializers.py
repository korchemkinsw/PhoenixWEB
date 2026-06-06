from rest_framework import serializers
from .models import Company, Groups, Panel

class ListGroupsForCompanySerializer(serializers.ModelSerializer):
  class Meta:
    model = Groups
    fields = ('group_field', 'message', 'disabled')
    
class ListCompanySerializer(serializers.ModelSerializer):
  panel = serializers.SerializerMethodField()
  test = serializers.SerializerMethodField()
  disabled = serializers.SerializerMethodField()
  groups = serializers.SerializerMethodField()

  def get_panel(self, obj):
    return obj.company_id.split('#', 1)[0]
  
  def get_test(self, obj):
    return Panel.objects.get(panel_id = obj.company_id.split('#', 1)[0]).testpanel
  
  def get_disabled(self, obj):
    return Panel.objects.get(panel_id = obj.company_id.split('#', 1)[0]).disabled

  def get_groups(self, obj):
    if Groups.objects.count():
      groups = Groups.objects.filter(company = obj.company_id)
      return ListGroupsForCompanySerializer(groups, many=True).data
    return []

  class Meta:
    model = Company
    fields = ('company_id', 'panel', 'test', 'disabled', 'companyname', 'address', 'groups')

class DetailCompanyMinSerializer(serializers.ModelSerializer):
  #company_id = serializers.SerializerMethodField()
  latitude = serializers.SerializerMethodField()
  longtitude = serializers.SerializerMethodField()
  operatorprompt = serializers.SerializerMethodField()
 
  #def get_company_id(self,obj):
  #  return obj.company_id.replace('#', '&')

  def get_latitude(self, obj):
    return Panel.objects.get(panel_id = obj.company_id.split('#', 1)[0]).latitude
    
  def get_longtitude(self, obj):
    return Panel.objects.get(panel_id = obj.company_id.split('#', 1)[0]).longtitude

  def get_operatorprompt(self, obj):
    return Groups.objects.get(panel = obj.company_id.split('#', 1)[0], group_field = obj.company_id.split('#', 1)[1]).operatorprompt
  
  class Meta:
    model = Company
    fields = ('company_id', 'companyname', 'address', 'latitude', 'longtitude', 'operatorprompt')
  