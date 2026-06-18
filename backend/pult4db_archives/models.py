import datetime

from django.db import models

class Archive(models.Model):
  event_id = models.IntegerField(db_column='Event_id', primary_key=True)  # Field name made lowercase.
  date_key = models.IntegerField(db_column='Date_Key')  # Field name made lowercase.
  panel_id = models.CharField(db_column='Panel_id', max_length=15, blank=True, null=True)  # Field name made lowercase.
  group_field = models.IntegerField(db_column='Group_', blank=True, null=True)  # Field name made lowercase. Field renamed because it ended with '_'.
  line = models.CharField(db_column='Line', max_length=10, blank=True, null=True)  # Field name made lowercase.
  zone = models.IntegerField(db_column='Zone', blank=True, null=True)  # Field name made lowercase.
  code = models.CharField(db_column='Code', max_length=6, blank=True, null=True)  # Field name made lowercase.
  codegroup = models.SmallIntegerField(db_column='CodeGroup', blank=True, null=True)  # Field name made lowercase.
  timeevent = models.DateTimeField(db_column='TimeEvent', blank=True, null=True)  # Field name made lowercase.
  phone = models.CharField(db_column='Phone', max_length=15, blank=True, null=True)  # Field name made lowercase.
  metercount = models.CharField(db_column='MeterCount', max_length=300, blank=True, null=True)  # Field name made lowercase.
  timemetercount = models.DateTimeField(db_column='TimeMeterCount', blank=True, null=True)  # Field name made lowercase.
  stateevent = models.SmallIntegerField(db_column='StateEvent', blank=True, null=True)  # Field name made lowercase.
  event_parent = models.ForeignKey('self', models.DO_NOTHING, db_column='Event_Parent_id', blank=True, null=True)  # Field name made lowercase.
  result_text = models.CharField(db_column='Result_Text', max_length=800, blank=True, null=True)  # Field name made lowercase.
  bitmask = models.IntegerField(db_column='BitMask')  # Field name made lowercase.
  deviceeventtime = models.DateTimeField(db_column='DeviceEventTime', blank=True, null=True)  # Field name made lowercase.

  class Meta:
    managed = False
    app_label = 'pult4db_archives'

def get_today_date_stamp():
  date_today = str(datetime.date.today())
  date_stamp = date_today.split('-', 2)[0] + date_today.split('-', 2)[1] + '01'
  return date_stamp

def get_archive_model(date_stamp):
  class Archive(models.Model):
    event_id = models.IntegerField(db_column='Event_id', primary_key=True)  # Field name made lowercase.
    date_key = models.IntegerField(db_column='Date_Key')  # Field name made lowercase.
    panel_id = models.CharField(db_column='Panel_id', max_length=15, blank=True, null=True)  # Field name made lowercase.
    group_field = models.IntegerField(db_column='Group_', blank=True, null=True)  # Field name made lowercase. Field renamed because it ended with '_'.
    line = models.CharField(db_column='Line', max_length=10, blank=True, null=True)  # Field name made lowercase.
    zone = models.IntegerField(db_column='Zone', blank=True, null=True)  # Field name made lowercase.
    code = models.CharField(db_column='Code', max_length=6, blank=True, null=True)  # Field name made lowercase.
    codegroup = models.SmallIntegerField(db_column='CodeGroup', blank=True, null=True)  # Field name made lowercase.
    timeevent = models.DateTimeField(db_column='TimeEvent', blank=True, null=True)  # Field name made lowercase.
    phone = models.CharField(db_column='Phone', max_length=15, blank=True, null=True)  # Field name made lowercase.
    metercount = models.CharField(db_column='MeterCount', max_length=300, blank=True, null=True)  # Field name made lowercase.
    timemetercount = models.DateTimeField(db_column='TimeMeterCount', blank=True, null=True)  # Field name made lowercase.
    stateevent = models.SmallIntegerField(db_column='StateEvent', blank=True, null=True)  # Field name made lowercase.
    event_parent = models.ForeignKey('self', models.DO_NOTHING, db_column='Event_Parent_id', blank=True, null=True)  # Field name made lowercase.
    result_text = models.CharField(db_column='Result_Text', max_length=800, blank=True, null=True)  # Field name made lowercase.
    bitmask = models.IntegerField(db_column='BitMask')  # Field name made lowercase.
    deviceeventtime = models.DateTimeField(db_column='DeviceEventTime', blank=True, null=True)  # Field name made lowercase.

    class Meta:
      managed = False
      app_label = 'pult4db_archives'
      db_table = f'archive{date_stamp}'

    def __str__(self):
      return f'{self.panel_id} {self.code} {self.group_field} {self.zone} {self.timeevent}'
       
  return Archive

def get_eventservice_model(date_stamp):
  class Eventservice(models.Model):
    service_id = models.AutoField(db_column='Service_id', primary_key=True)  # Field name made lowercase.
    namestate = models.CharField(db_column='NameState', max_length=60, blank=True, null=True)  # Field name made lowercase.
    event = models.ForeignKey(get_archive_model(date_stamp), models.DO_NOTHING, db_column='Event_id')  # Field name made lowercase.
    computer = models.CharField(db_column='Computer', max_length=50)  # Field name made lowercase.
    operationtime = models.DateTimeField(db_column='OperationTime')  # Field name made lowercase.
    date_key = models.IntegerField(db_column='Date_Key')  # Field name made lowercase.
    personname = models.CharField(db_column='PersonName', max_length=200, blank=True, null=True)  # Field name made lowercase.
    grresponsename = models.CharField(db_column='GrResponseName', max_length=100, blank=True, null=True)  # Field name made lowercase.

    class Meta:
      managed = False
      db_table = f'eventservice{date_stamp}'
  return Eventservice
  