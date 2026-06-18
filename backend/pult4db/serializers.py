from rest_framework import serializers
from .models import Code, Company, Groupresponse, Groups, Panel, Zones
from pult4db_archives.models import get_today_date_stamp, get_archive_model

class ListGroupsSerializer(serializers.ModelSerializer):
  class Meta:
    model = Groups
    fields = ('panel', 'group_field', 'message', 'disabled')

class AlertGroupSerializer(serializers.ModelSerializer):
  company_id = serializers.SerializerMethodField()
  companyname = serializers.SerializerMethodField()
  address = serializers.SerializerMethodField()
  latitude = serializers.SerializerMethodField()
  longtitude = serializers.SerializerMethodField()

  def get_company_id(self,obj):
    return obj.company.company_id

  def get_companyname(self, obj):
    return obj.company.companyname
  
  def get_address(self, obj):
    return obj.company.address
  
  def get_latitude(self, obj):
    return obj.panel.latitude
  
  def get_longtitude(self, obj):
    return obj.panel.longtitude
  
  class Meta:
    model = Groups
    fields = ('company_id', 'group_field', 'companyname', 'address', 'latitude', 'longtitude', 'operatorprompt')
    
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
    return Panel.objects.using('pult4db').get(panel_id = obj.company_id.split('#', 1)[0]).latitude
    
  def get_longtitude(self, obj):
    return Panel.objects.using('pult4db').get(panel_id = obj.company_id.split('#', 1)[0]).longtitude

  def get_operatorprompt(self, obj):
    return Groups.objects.using('pult4db').get(panel = obj.company_id.split('#', 1)[0], group_field = obj.company_id.split('#', 1)[1]).operatorprompt
  
  class Meta:
    model = Company
    fields = ('company_id', 'companyname', 'address', 'latitude', 'longtitude', 'operatorprompt')

class ListGroupResponseSerializer(serializers.ModelSerializer):
  company = serializers.SerializerMethodField()
  message = serializers.SerializerMethodField()
  event = serializers.SerializerMethodField()

  def get_company(self, obj):
    if obj.panel_id:
      group = Groups.objects.using('pult4db').get(panel = obj.panel_id, group_field = obj.group_field)
      return AlertGroupSerializer(group, read_only=True).data
    return {}
  
  def get_message(self, obj):
    if obj.group_field:
      group = Groups.objects.using('pult4db').get(panel = obj.panel_id, group_field = obj.group_field)
      return group.message
    return ''
  
  def get_event(self, obj):
    date_stamp = get_today_date_stamp()
    Events = get_archive_model(date_stamp)
    event = Events.objects.filter(event_id = obj.event_id).first()
    if event != None:
      codes = Code.objects.using('pult4db').filter(codegroup = 1).filter(code = event.code) #filter(codegroup = 1).
      if (len(codes) != 0):
        code = codes[0].message
        zone = Zones.objects.using('pult4db').get(panel = event.panel_id, group_field = event.group_field, zone = event.zone).message
        if str(codes[0].code)[:1] != 'E' or len(zone) < 2:
          return code
        return zone
    return ''
    
  class Meta:
    model = Groupresponse
    fields = ('group_id', 'description', 'status', 'panel_id', 'message', 'event', 'company')
  