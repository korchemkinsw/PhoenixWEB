# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Archive20230101(models.Model):
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
        db_table = 'archive20230101'


class Archive20230201(models.Model):
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
        db_table = 'archive20230201'


class Archive20230301(models.Model):
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
        db_table = 'archive20230301'


class Archive20230401(models.Model):
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
        db_table = 'archive20230401'


class Archive20230501(models.Model):
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
        db_table = 'archive20230501'


class Archive20230601(models.Model):
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
        db_table = 'archive20230601'


class Archive20230701(models.Model):
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
        db_table = 'archive20230701'


class Archive20230801(models.Model):
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
        db_table = 'archive20230801'


class Archive20230901(models.Model):
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
        db_table = 'archive20230901'


class Archive20231001(models.Model):
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
        db_table = 'archive20231001'


class Archive20231101(models.Model):
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
        db_table = 'archive20231101'


class Archive20231201(models.Model):
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
        db_table = 'archive20231201'


class Archive20240101(models.Model):
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
        db_table = 'archive20240101'


class Archive20240201(models.Model):
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
        db_table = 'archive20240201'


class Archive20240301(models.Model):
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
        db_table = 'archive20240301'


class Archive20240401(models.Model):
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
        db_table = 'archive20240401'


class Archive20240501(models.Model):
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
        db_table = 'archive20240501'


class Archive20240601(models.Model):
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
        db_table = 'archive20240601'


class Archive20240701(models.Model):
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
        db_table = 'archive20240701'


class Archive20240801(models.Model):
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
        db_table = 'archive20240801'


class Archive20240901(models.Model):
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
        db_table = 'archive20240901'


class Archive20241001(models.Model):
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
        db_table = 'archive20241001'


class Archive20241101(models.Model):
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
        db_table = 'archive20241101'


class Archive20241201(models.Model):
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
        db_table = 'archive20241201'


class Archive20250101(models.Model):
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
        db_table = 'archive20250101'


class Archive20250201(models.Model):
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
        db_table = 'archive20250201'


class Archive20250301(models.Model):
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
        db_table = 'archive20250301'


class Archive20250401(models.Model):
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
        db_table = 'archive20250401'


class Archive20250501(models.Model):
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
        db_table = 'archive20250501'


class Archive20250601(models.Model):
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
        db_table = 'archive20250601'


class Archive20250701(models.Model):
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
        db_table = 'archive20250701'


class Archive20250801(models.Model):
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
        db_table = 'archive20250801'


class Archive20250901(models.Model):
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
        db_table = 'archive20250901'


class Archive20251001(models.Model):
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
        db_table = 'archive20251001'


class Archive20251101(models.Model):
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
        db_table = 'archive20251101'


class Archive20251201(models.Model):
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
        db_table = 'archive20251201'


class Archive20260101(models.Model):
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
        db_table = 'archive20260101'


class Archive20260201(models.Model):
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
        db_table = 'archive20260201'


class Archive20260301(models.Model):
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
        db_table = 'archive20260301'


class Eventservice20230101(models.Model):
    service_id = models.AutoField(db_column='Service_id', primary_key=True)  # Field name made lowercase.
    namestate = models.CharField(db_column='NameState', max_length=60, blank=True, null=True)  # Field name made lowercase.
    event = models.ForeignKey(Archive20230101, models.DO_NOTHING, db_column='Event_id')  # Field name made lowercase.
    computer = models.CharField(db_column='Computer', max_length=50)  # Field name made lowercase.
    operationtime = models.DateTimeField(db_column='OperationTime')  # Field name made lowercase.
    date_key = models.IntegerField(db_column='Date_Key')  # Field name made lowercase.
    personname = models.CharField(db_column='PersonName', max_length=200, blank=True, null=True)  # Field name made lowercase.
    grresponsename = models.CharField(db_column='GrResponseName', max_length=100, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'eventservice20230101'


class Eventservice20230201(models.Model):
    service_id = models.AutoField(db_column='Service_id', primary_key=True)  # Field name made lowercase.
    namestate = models.CharField(db_column='NameState', max_length=60, blank=True, null=True)  # Field name made lowercase.
    event = models.ForeignKey(Archive20230201, models.DO_NOTHING, db_column='Event_id')  # Field name made lowercase.
    computer = models.CharField(db_column='Computer', max_length=50)  # Field name made lowercase.
    operationtime = models.DateTimeField(db_column='OperationTime')  # Field name made lowercase.
    date_key = models.IntegerField(db_column='Date_Key')  # Field name made lowercase.
    personname = models.CharField(db_column='PersonName', max_length=200, blank=True, null=True)  # Field name made lowercase.
    grresponsename = models.CharField(db_column='GrResponseName', max_length=100, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'eventservice20230201'


class Eventservice20230301(models.Model):
    service_id = models.AutoField(db_column='Service_id', primary_key=True)  # Field name made lowercase.
    namestate = models.CharField(db_column='NameState', max_length=60, blank=True, null=True)  # Field name made lowercase.
    event = models.ForeignKey(Archive20230301, models.DO_NOTHING, db_column='Event_id')  # Field name made lowercase.
    computer = models.CharField(db_column='Computer', max_length=50)  # Field name made lowercase.
    operationtime = models.DateTimeField(db_column='OperationTime')  # Field name made lowercase.
    date_key = models.IntegerField(db_column='Date_Key')  # Field name made lowercase.
    personname = models.CharField(db_column='PersonName', max_length=200, blank=True, null=True)  # Field name made lowercase.
    grresponsename = models.CharField(db_column='GrResponseName', max_length=100, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'eventservice20230301'


class Eventservice20230401(models.Model):
    service_id = models.AutoField(db_column='Service_id', primary_key=True)  # Field name made lowercase.
    namestate = models.CharField(db_column='NameState', max_length=60, blank=True, null=True)  # Field name made lowercase.
    event = models.ForeignKey(Archive20230401, models.DO_NOTHING, db_column='Event_id')  # Field name made lowercase.
    computer = models.CharField(db_column='Computer', max_length=50)  # Field name made lowercase.
    operationtime = models.DateTimeField(db_column='OperationTime')  # Field name made lowercase.
    date_key = models.IntegerField(db_column='Date_Key')  # Field name made lowercase.
    personname = models.CharField(db_column='PersonName', max_length=200, blank=True, null=True)  # Field name made lowercase.
    grresponsename = models.CharField(db_column='GrResponseName', max_length=100, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'eventservice20230401'


class Eventservice20230501(models.Model):
    service_id = models.AutoField(db_column='Service_id', primary_key=True)  # Field name made lowercase.
    namestate = models.CharField(db_column='NameState', max_length=60, blank=True, null=True)  # Field name made lowercase.
    event = models.ForeignKey(Archive20230501, models.DO_NOTHING, db_column='Event_id')  # Field name made lowercase.
    computer = models.CharField(db_column='Computer', max_length=50)  # Field name made lowercase.
    operationtime = models.DateTimeField(db_column='OperationTime')  # Field name made lowercase.
    date_key = models.IntegerField(db_column='Date_Key')  # Field name made lowercase.
    personname = models.CharField(db_column='PersonName', max_length=200, blank=True, null=True)  # Field name made lowercase.
    grresponsename = models.CharField(db_column='GrResponseName', max_length=100, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'eventservice20230501'


class Eventservice20230601(models.Model):
    service_id = models.AutoField(db_column='Service_id', primary_key=True)  # Field name made lowercase.
    namestate = models.CharField(db_column='NameState', max_length=60, blank=True, null=True)  # Field name made lowercase.
    event = models.ForeignKey(Archive20230601, models.DO_NOTHING, db_column='Event_id')  # Field name made lowercase.
    computer = models.CharField(db_column='Computer', max_length=50)  # Field name made lowercase.
    operationtime = models.DateTimeField(db_column='OperationTime')  # Field name made lowercase.
    date_key = models.IntegerField(db_column='Date_Key')  # Field name made lowercase.
    personname = models.CharField(db_column='PersonName', max_length=200, blank=True, null=True)  # Field name made lowercase.
    grresponsename = models.CharField(db_column='GrResponseName', max_length=100, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'eventservice20230601'


class Eventservice20230701(models.Model):
    service_id = models.AutoField(db_column='Service_id', primary_key=True)  # Field name made lowercase.
    namestate = models.CharField(db_column='NameState', max_length=60, blank=True, null=True)  # Field name made lowercase.
    event = models.ForeignKey(Archive20230701, models.DO_NOTHING, db_column='Event_id')  # Field name made lowercase.
    computer = models.CharField(db_column='Computer', max_length=50)  # Field name made lowercase.
    operationtime = models.DateTimeField(db_column='OperationTime')  # Field name made lowercase.
    date_key = models.IntegerField(db_column='Date_Key')  # Field name made lowercase.
    personname = models.CharField(db_column='PersonName', max_length=200, blank=True, null=True)  # Field name made lowercase.
    grresponsename = models.CharField(db_column='GrResponseName', max_length=100, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'eventservice20230701'


class Eventservice20230801(models.Model):
    service_id = models.AutoField(db_column='Service_id', primary_key=True)  # Field name made lowercase.
    namestate = models.CharField(db_column='NameState', max_length=60, blank=True, null=True)  # Field name made lowercase.
    event = models.ForeignKey(Archive20230801, models.DO_NOTHING, db_column='Event_id')  # Field name made lowercase.
    computer = models.CharField(db_column='Computer', max_length=50)  # Field name made lowercase.
    operationtime = models.DateTimeField(db_column='OperationTime')  # Field name made lowercase.
    date_key = models.IntegerField(db_column='Date_Key')  # Field name made lowercase.
    personname = models.CharField(db_column='PersonName', max_length=200, blank=True, null=True)  # Field name made lowercase.
    grresponsename = models.CharField(db_column='GrResponseName', max_length=100, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'eventservice20230801'


class Eventservice20230901(models.Model):
    service_id = models.AutoField(db_column='Service_id', primary_key=True)  # Field name made lowercase.
    namestate = models.CharField(db_column='NameState', max_length=60, blank=True, null=True)  # Field name made lowercase.
    event = models.ForeignKey(Archive20230901, models.DO_NOTHING, db_column='Event_id')  # Field name made lowercase.
    computer = models.CharField(db_column='Computer', max_length=50)  # Field name made lowercase.
    operationtime = models.DateTimeField(db_column='OperationTime')  # Field name made lowercase.
    date_key = models.IntegerField(db_column='Date_Key')  # Field name made lowercase.
    personname = models.CharField(db_column='PersonName', max_length=200, blank=True, null=True)  # Field name made lowercase.
    grresponsename = models.CharField(db_column='GrResponseName', max_length=100, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'eventservice20230901'


class Eventservice20231001(models.Model):
    service_id = models.AutoField(db_column='Service_id', primary_key=True)  # Field name made lowercase.
    namestate = models.CharField(db_column='NameState', max_length=60, blank=True, null=True)  # Field name made lowercase.
    event = models.ForeignKey(Archive20231001, models.DO_NOTHING, db_column='Event_id')  # Field name made lowercase.
    computer = models.CharField(db_column='Computer', max_length=50)  # Field name made lowercase.
    operationtime = models.DateTimeField(db_column='OperationTime')  # Field name made lowercase.
    date_key = models.IntegerField(db_column='Date_Key')  # Field name made lowercase.
    personname = models.CharField(db_column='PersonName', max_length=200, blank=True, null=True)  # Field name made lowercase.
    grresponsename = models.CharField(db_column='GrResponseName', max_length=100, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'eventservice20231001'


class Eventservice20231101(models.Model):
    service_id = models.AutoField(db_column='Service_id', primary_key=True)  # Field name made lowercase.
    namestate = models.CharField(db_column='NameState', max_length=60, blank=True, null=True)  # Field name made lowercase.
    event = models.ForeignKey(Archive20231101, models.DO_NOTHING, db_column='Event_id')  # Field name made lowercase.
    computer = models.CharField(db_column='Computer', max_length=50)  # Field name made lowercase.
    operationtime = models.DateTimeField(db_column='OperationTime')  # Field name made lowercase.
    date_key = models.IntegerField(db_column='Date_Key')  # Field name made lowercase.
    personname = models.CharField(db_column='PersonName', max_length=200, blank=True, null=True)  # Field name made lowercase.
    grresponsename = models.CharField(db_column='GrResponseName', max_length=100, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'eventservice20231101'


class Eventservice20231201(models.Model):
    service_id = models.AutoField(db_column='Service_id', primary_key=True)  # Field name made lowercase.
    namestate = models.CharField(db_column='NameState', max_length=60, blank=True, null=True)  # Field name made lowercase.
    event = models.ForeignKey(Archive20231201, models.DO_NOTHING, db_column='Event_id')  # Field name made lowercase.
    computer = models.CharField(db_column='Computer', max_length=50)  # Field name made lowercase.
    operationtime = models.DateTimeField(db_column='OperationTime')  # Field name made lowercase.
    date_key = models.IntegerField(db_column='Date_Key')  # Field name made lowercase.
    personname = models.CharField(db_column='PersonName', max_length=200, blank=True, null=True)  # Field name made lowercase.
    grresponsename = models.CharField(db_column='GrResponseName', max_length=100, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'eventservice20231201'


class Eventservice20240101(models.Model):
    service_id = models.AutoField(db_column='Service_id', primary_key=True)  # Field name made lowercase.
    namestate = models.CharField(db_column='NameState', max_length=60, blank=True, null=True)  # Field name made lowercase.
    event = models.ForeignKey(Archive20240101, models.DO_NOTHING, db_column='Event_id')  # Field name made lowercase.
    computer = models.CharField(db_column='Computer', max_length=50)  # Field name made lowercase.
    operationtime = models.DateTimeField(db_column='OperationTime')  # Field name made lowercase.
    date_key = models.IntegerField(db_column='Date_Key')  # Field name made lowercase.
    personname = models.CharField(db_column='PersonName', max_length=200, blank=True, null=True)  # Field name made lowercase.
    grresponsename = models.CharField(db_column='GrResponseName', max_length=100, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'eventservice20240101'


class Eventservice20240201(models.Model):
    service_id = models.AutoField(db_column='Service_id', primary_key=True)  # Field name made lowercase.
    namestate = models.CharField(db_column='NameState', max_length=60, blank=True, null=True)  # Field name made lowercase.
    event = models.ForeignKey(Archive20240201, models.DO_NOTHING, db_column='Event_id')  # Field name made lowercase.
    computer = models.CharField(db_column='Computer', max_length=50)  # Field name made lowercase.
    operationtime = models.DateTimeField(db_column='OperationTime')  # Field name made lowercase.
    date_key = models.IntegerField(db_column='Date_Key')  # Field name made lowercase.
    personname = models.CharField(db_column='PersonName', max_length=200, blank=True, null=True)  # Field name made lowercase.
    grresponsename = models.CharField(db_column='GrResponseName', max_length=100, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'eventservice20240201'


class Eventservice20240301(models.Model):
    service_id = models.AutoField(db_column='Service_id', primary_key=True)  # Field name made lowercase.
    namestate = models.CharField(db_column='NameState', max_length=60, blank=True, null=True)  # Field name made lowercase.
    event = models.ForeignKey(Archive20240301, models.DO_NOTHING, db_column='Event_id')  # Field name made lowercase.
    computer = models.CharField(db_column='Computer', max_length=50)  # Field name made lowercase.
    operationtime = models.DateTimeField(db_column='OperationTime')  # Field name made lowercase.
    date_key = models.IntegerField(db_column='Date_Key')  # Field name made lowercase.
    personname = models.CharField(db_column='PersonName', max_length=200, blank=True, null=True)  # Field name made lowercase.
    grresponsename = models.CharField(db_column='GrResponseName', max_length=100, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'eventservice20240301'


class Eventservice20240401(models.Model):
    service_id = models.AutoField(db_column='Service_id', primary_key=True)  # Field name made lowercase.
    namestate = models.CharField(db_column='NameState', max_length=60, blank=True, null=True)  # Field name made lowercase.
    event = models.ForeignKey(Archive20240401, models.DO_NOTHING, db_column='Event_id')  # Field name made lowercase.
    computer = models.CharField(db_column='Computer', max_length=50)  # Field name made lowercase.
    operationtime = models.DateTimeField(db_column='OperationTime')  # Field name made lowercase.
    date_key = models.IntegerField(db_column='Date_Key')  # Field name made lowercase.
    personname = models.CharField(db_column='PersonName', max_length=200, blank=True, null=True)  # Field name made lowercase.
    grresponsename = models.CharField(db_column='GrResponseName', max_length=100, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'eventservice20240401'


class Eventservice20240501(models.Model):
    service_id = models.AutoField(db_column='Service_id', primary_key=True)  # Field name made lowercase.
    namestate = models.CharField(db_column='NameState', max_length=60, blank=True, null=True)  # Field name made lowercase.
    event = models.ForeignKey(Archive20240501, models.DO_NOTHING, db_column='Event_id')  # Field name made lowercase.
    computer = models.CharField(db_column='Computer', max_length=50)  # Field name made lowercase.
    operationtime = models.DateTimeField(db_column='OperationTime')  # Field name made lowercase.
    date_key = models.IntegerField(db_column='Date_Key')  # Field name made lowercase.
    personname = models.CharField(db_column='PersonName', max_length=200, blank=True, null=True)  # Field name made lowercase.
    grresponsename = models.CharField(db_column='GrResponseName', max_length=100, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'eventservice20240501'


class Eventservice20240601(models.Model):
    service_id = models.AutoField(db_column='Service_id', primary_key=True)  # Field name made lowercase.
    namestate = models.CharField(db_column='NameState', max_length=60, blank=True, null=True)  # Field name made lowercase.
    event = models.ForeignKey(Archive20240601, models.DO_NOTHING, db_column='Event_id')  # Field name made lowercase.
    computer = models.CharField(db_column='Computer', max_length=50)  # Field name made lowercase.
    operationtime = models.DateTimeField(db_column='OperationTime')  # Field name made lowercase.
    date_key = models.IntegerField(db_column='Date_Key')  # Field name made lowercase.
    personname = models.CharField(db_column='PersonName', max_length=200, blank=True, null=True)  # Field name made lowercase.
    grresponsename = models.CharField(db_column='GrResponseName', max_length=100, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'eventservice20240601'


class Eventservice20240701(models.Model):
    service_id = models.AutoField(db_column='Service_id', primary_key=True)  # Field name made lowercase.
    namestate = models.CharField(db_column='NameState', max_length=60, blank=True, null=True)  # Field name made lowercase.
    event = models.ForeignKey(Archive20240701, models.DO_NOTHING, db_column='Event_id')  # Field name made lowercase.
    computer = models.CharField(db_column='Computer', max_length=50)  # Field name made lowercase.
    operationtime = models.DateTimeField(db_column='OperationTime')  # Field name made lowercase.
    date_key = models.IntegerField(db_column='Date_Key')  # Field name made lowercase.
    personname = models.CharField(db_column='PersonName', max_length=200, blank=True, null=True)  # Field name made lowercase.
    grresponsename = models.CharField(db_column='GrResponseName', max_length=100, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'eventservice20240701'


class Eventservice20240801(models.Model):
    service_id = models.AutoField(db_column='Service_id', primary_key=True)  # Field name made lowercase.
    namestate = models.CharField(db_column='NameState', max_length=60, blank=True, null=True)  # Field name made lowercase.
    event = models.ForeignKey(Archive20240801, models.DO_NOTHING, db_column='Event_id')  # Field name made lowercase.
    computer = models.CharField(db_column='Computer', max_length=50)  # Field name made lowercase.
    operationtime = models.DateTimeField(db_column='OperationTime')  # Field name made lowercase.
    date_key = models.IntegerField(db_column='Date_Key')  # Field name made lowercase.
    personname = models.CharField(db_column='PersonName', max_length=200, blank=True, null=True)  # Field name made lowercase.
    grresponsename = models.CharField(db_column='GrResponseName', max_length=100, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'eventservice20240801'


class Eventservice20240901(models.Model):
    service_id = models.AutoField(db_column='Service_id', primary_key=True)  # Field name made lowercase.
    namestate = models.CharField(db_column='NameState', max_length=60, blank=True, null=True)  # Field name made lowercase.
    event = models.ForeignKey(Archive20240901, models.DO_NOTHING, db_column='Event_id')  # Field name made lowercase.
    computer = models.CharField(db_column='Computer', max_length=50)  # Field name made lowercase.
    operationtime = models.DateTimeField(db_column='OperationTime')  # Field name made lowercase.
    date_key = models.IntegerField(db_column='Date_Key')  # Field name made lowercase.
    personname = models.CharField(db_column='PersonName', max_length=200, blank=True, null=True)  # Field name made lowercase.
    grresponsename = models.CharField(db_column='GrResponseName', max_length=100, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'eventservice20240901'


class Eventservice20241001(models.Model):
    service_id = models.AutoField(db_column='Service_id', primary_key=True)  # Field name made lowercase.
    namestate = models.CharField(db_column='NameState', max_length=60, blank=True, null=True)  # Field name made lowercase.
    event = models.ForeignKey(Archive20241001, models.DO_NOTHING, db_column='Event_id')  # Field name made lowercase.
    computer = models.CharField(db_column='Computer', max_length=50)  # Field name made lowercase.
    operationtime = models.DateTimeField(db_column='OperationTime')  # Field name made lowercase.
    date_key = models.IntegerField(db_column='Date_Key')  # Field name made lowercase.
    personname = models.CharField(db_column='PersonName', max_length=200, blank=True, null=True)  # Field name made lowercase.
    grresponsename = models.CharField(db_column='GrResponseName', max_length=100, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'eventservice20241001'


class Eventservice20241101(models.Model):
    service_id = models.AutoField(db_column='Service_id', primary_key=True)  # Field name made lowercase.
    namestate = models.CharField(db_column='NameState', max_length=60, blank=True, null=True)  # Field name made lowercase.
    event = models.ForeignKey(Archive20241101, models.DO_NOTHING, db_column='Event_id')  # Field name made lowercase.
    computer = models.CharField(db_column='Computer', max_length=50)  # Field name made lowercase.
    operationtime = models.DateTimeField(db_column='OperationTime')  # Field name made lowercase.
    date_key = models.IntegerField(db_column='Date_Key')  # Field name made lowercase.
    personname = models.CharField(db_column='PersonName', max_length=200, blank=True, null=True)  # Field name made lowercase.
    grresponsename = models.CharField(db_column='GrResponseName', max_length=100, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'eventservice20241101'


class Eventservice20241201(models.Model):
    service_id = models.AutoField(db_column='Service_id', primary_key=True)  # Field name made lowercase.
    namestate = models.CharField(db_column='NameState', max_length=60, blank=True, null=True)  # Field name made lowercase.
    event = models.ForeignKey(Archive20241201, models.DO_NOTHING, db_column='Event_id')  # Field name made lowercase.
    computer = models.CharField(db_column='Computer', max_length=50)  # Field name made lowercase.
    operationtime = models.DateTimeField(db_column='OperationTime')  # Field name made lowercase.
    date_key = models.IntegerField(db_column='Date_Key')  # Field name made lowercase.
    personname = models.CharField(db_column='PersonName', max_length=200, blank=True, null=True)  # Field name made lowercase.
    grresponsename = models.CharField(db_column='GrResponseName', max_length=100, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'eventservice20241201'


class Eventservice20250101(models.Model):
    service_id = models.AutoField(db_column='Service_id', primary_key=True)  # Field name made lowercase.
    namestate = models.CharField(db_column='NameState', max_length=60, blank=True, null=True)  # Field name made lowercase.
    event = models.ForeignKey(Archive20250101, models.DO_NOTHING, db_column='Event_id')  # Field name made lowercase.
    computer = models.CharField(db_column='Computer', max_length=50)  # Field name made lowercase.
    operationtime = models.DateTimeField(db_column='OperationTime')  # Field name made lowercase.
    date_key = models.IntegerField(db_column='Date_Key')  # Field name made lowercase.
    personname = models.CharField(db_column='PersonName', max_length=200, blank=True, null=True)  # Field name made lowercase.
    grresponsename = models.CharField(db_column='GrResponseName', max_length=100, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'eventservice20250101'


class Eventservice20250201(models.Model):
    service_id = models.AutoField(db_column='Service_id', primary_key=True)  # Field name made lowercase.
    namestate = models.CharField(db_column='NameState', max_length=60, blank=True, null=True)  # Field name made lowercase.
    event = models.ForeignKey(Archive20250201, models.DO_NOTHING, db_column='Event_id')  # Field name made lowercase.
    computer = models.CharField(db_column='Computer', max_length=50)  # Field name made lowercase.
    operationtime = models.DateTimeField(db_column='OperationTime')  # Field name made lowercase.
    date_key = models.IntegerField(db_column='Date_Key')  # Field name made lowercase.
    personname = models.CharField(db_column='PersonName', max_length=200, blank=True, null=True)  # Field name made lowercase.
    grresponsename = models.CharField(db_column='GrResponseName', max_length=100, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'eventservice20250201'


class Eventservice20250301(models.Model):
    service_id = models.AutoField(db_column='Service_id', primary_key=True)  # Field name made lowercase.
    namestate = models.CharField(db_column='NameState', max_length=60, blank=True, null=True)  # Field name made lowercase.
    event = models.ForeignKey(Archive20250301, models.DO_NOTHING, db_column='Event_id')  # Field name made lowercase.
    computer = models.CharField(db_column='Computer', max_length=50)  # Field name made lowercase.
    operationtime = models.DateTimeField(db_column='OperationTime')  # Field name made lowercase.
    date_key = models.IntegerField(db_column='Date_Key')  # Field name made lowercase.
    personname = models.CharField(db_column='PersonName', max_length=200, blank=True, null=True)  # Field name made lowercase.
    grresponsename = models.CharField(db_column='GrResponseName', max_length=100, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'eventservice20250301'


class Eventservice20250401(models.Model):
    service_id = models.AutoField(db_column='Service_id', primary_key=True)  # Field name made lowercase.
    namestate = models.CharField(db_column='NameState', max_length=60, blank=True, null=True)  # Field name made lowercase.
    event = models.ForeignKey(Archive20250401, models.DO_NOTHING, db_column='Event_id')  # Field name made lowercase.
    computer = models.CharField(db_column='Computer', max_length=50)  # Field name made lowercase.
    operationtime = models.DateTimeField(db_column='OperationTime')  # Field name made lowercase.
    date_key = models.IntegerField(db_column='Date_Key')  # Field name made lowercase.
    personname = models.CharField(db_column='PersonName', max_length=200, blank=True, null=True)  # Field name made lowercase.
    grresponsename = models.CharField(db_column='GrResponseName', max_length=100, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'eventservice20250401'


class Eventservice20250501(models.Model):
    service_id = models.AutoField(db_column='Service_id', primary_key=True)  # Field name made lowercase.
    namestate = models.CharField(db_column='NameState', max_length=60, blank=True, null=True)  # Field name made lowercase.
    event = models.ForeignKey(Archive20250501, models.DO_NOTHING, db_column='Event_id')  # Field name made lowercase.
    computer = models.CharField(db_column='Computer', max_length=50)  # Field name made lowercase.
    operationtime = models.DateTimeField(db_column='OperationTime')  # Field name made lowercase.
    date_key = models.IntegerField(db_column='Date_Key')  # Field name made lowercase.
    personname = models.CharField(db_column='PersonName', max_length=200, blank=True, null=True)  # Field name made lowercase.
    grresponsename = models.CharField(db_column='GrResponseName', max_length=100, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'eventservice20250501'


class Eventservice20250601(models.Model):
    service_id = models.AutoField(db_column='Service_id', primary_key=True)  # Field name made lowercase.
    namestate = models.CharField(db_column='NameState', max_length=60, blank=True, null=True)  # Field name made lowercase.
    event = models.ForeignKey(Archive20250601, models.DO_NOTHING, db_column='Event_id')  # Field name made lowercase.
    computer = models.CharField(db_column='Computer', max_length=50)  # Field name made lowercase.
    operationtime = models.DateTimeField(db_column='OperationTime')  # Field name made lowercase.
    date_key = models.IntegerField(db_column='Date_Key')  # Field name made lowercase.
    personname = models.CharField(db_column='PersonName', max_length=200, blank=True, null=True)  # Field name made lowercase.
    grresponsename = models.CharField(db_column='GrResponseName', max_length=100, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'eventservice20250601'


class Eventservice20250701(models.Model):
    service_id = models.AutoField(db_column='Service_id', primary_key=True)  # Field name made lowercase.
    namestate = models.CharField(db_column='NameState', max_length=60, blank=True, null=True)  # Field name made lowercase.
    event = models.ForeignKey(Archive20250701, models.DO_NOTHING, db_column='Event_id')  # Field name made lowercase.
    computer = models.CharField(db_column='Computer', max_length=50)  # Field name made lowercase.
    operationtime = models.DateTimeField(db_column='OperationTime')  # Field name made lowercase.
    date_key = models.IntegerField(db_column='Date_Key')  # Field name made lowercase.
    personname = models.CharField(db_column='PersonName', max_length=200, blank=True, null=True)  # Field name made lowercase.
    grresponsename = models.CharField(db_column='GrResponseName', max_length=100, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'eventservice20250701'


class Eventservice20250801(models.Model):
    service_id = models.AutoField(db_column='Service_id', primary_key=True)  # Field name made lowercase.
    namestate = models.CharField(db_column='NameState', max_length=60, blank=True, null=True)  # Field name made lowercase.
    event = models.ForeignKey(Archive20250801, models.DO_NOTHING, db_column='Event_id')  # Field name made lowercase.
    computer = models.CharField(db_column='Computer', max_length=50)  # Field name made lowercase.
    operationtime = models.DateTimeField(db_column='OperationTime')  # Field name made lowercase.
    date_key = models.IntegerField(db_column='Date_Key')  # Field name made lowercase.
    personname = models.CharField(db_column='PersonName', max_length=200, blank=True, null=True)  # Field name made lowercase.
    grresponsename = models.CharField(db_column='GrResponseName', max_length=100, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'eventservice20250801'


class Eventservice20250901(models.Model):
    service_id = models.AutoField(db_column='Service_id', primary_key=True)  # Field name made lowercase.
    namestate = models.CharField(db_column='NameState', max_length=60, blank=True, null=True)  # Field name made lowercase.
    event = models.ForeignKey(Archive20250901, models.DO_NOTHING, db_column='Event_id')  # Field name made lowercase.
    computer = models.CharField(db_column='Computer', max_length=50)  # Field name made lowercase.
    operationtime = models.DateTimeField(db_column='OperationTime')  # Field name made lowercase.
    date_key = models.IntegerField(db_column='Date_Key')  # Field name made lowercase.
    personname = models.CharField(db_column='PersonName', max_length=200, blank=True, null=True)  # Field name made lowercase.
    grresponsename = models.CharField(db_column='GrResponseName', max_length=100, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'eventservice20250901'


class Eventservice20251001(models.Model):
    service_id = models.AutoField(db_column='Service_id', primary_key=True)  # Field name made lowercase.
    namestate = models.CharField(db_column='NameState', max_length=60, blank=True, null=True)  # Field name made lowercase.
    event = models.ForeignKey(Archive20251001, models.DO_NOTHING, db_column='Event_id')  # Field name made lowercase.
    computer = models.CharField(db_column='Computer', max_length=50)  # Field name made lowercase.
    operationtime = models.DateTimeField(db_column='OperationTime')  # Field name made lowercase.
    date_key = models.IntegerField(db_column='Date_Key')  # Field name made lowercase.
    personname = models.CharField(db_column='PersonName', max_length=200, blank=True, null=True)  # Field name made lowercase.
    grresponsename = models.CharField(db_column='GrResponseName', max_length=100, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'eventservice20251001'


class Eventservice20251101(models.Model):
    service_id = models.AutoField(db_column='Service_id', primary_key=True)  # Field name made lowercase.
    namestate = models.CharField(db_column='NameState', max_length=60, blank=True, null=True)  # Field name made lowercase.
    event = models.ForeignKey(Archive20251101, models.DO_NOTHING, db_column='Event_id')  # Field name made lowercase.
    computer = models.CharField(db_column='Computer', max_length=50)  # Field name made lowercase.
    operationtime = models.DateTimeField(db_column='OperationTime')  # Field name made lowercase.
    date_key = models.IntegerField(db_column='Date_Key')  # Field name made lowercase.
    personname = models.CharField(db_column='PersonName', max_length=200, blank=True, null=True)  # Field name made lowercase.
    grresponsename = models.CharField(db_column='GrResponseName', max_length=100, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'eventservice20251101'


class Eventservice20251201(models.Model):
    service_id = models.AutoField(db_column='Service_id', primary_key=True)  # Field name made lowercase.
    namestate = models.CharField(db_column='NameState', max_length=60, blank=True, null=True)  # Field name made lowercase.
    event = models.ForeignKey(Archive20251201, models.DO_NOTHING, db_column='Event_id')  # Field name made lowercase.
    computer = models.CharField(db_column='Computer', max_length=50)  # Field name made lowercase.
    operationtime = models.DateTimeField(db_column='OperationTime')  # Field name made lowercase.
    date_key = models.IntegerField(db_column='Date_Key')  # Field name made lowercase.
    personname = models.CharField(db_column='PersonName', max_length=200, blank=True, null=True)  # Field name made lowercase.
    grresponsename = models.CharField(db_column='GrResponseName', max_length=100, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'eventservice20251201'


class Eventservice20260101(models.Model):
    service_id = models.AutoField(db_column='Service_id', primary_key=True)  # Field name made lowercase.
    namestate = models.CharField(db_column='NameState', max_length=60, blank=True, null=True)  # Field name made lowercase.
    event = models.ForeignKey(Archive20260101, models.DO_NOTHING, db_column='Event_id')  # Field name made lowercase.
    computer = models.CharField(db_column='Computer', max_length=50)  # Field name made lowercase.
    operationtime = models.DateTimeField(db_column='OperationTime')  # Field name made lowercase.
    date_key = models.IntegerField(db_column='Date_Key')  # Field name made lowercase.
    personname = models.CharField(db_column='PersonName', max_length=200, blank=True, null=True)  # Field name made lowercase.
    grresponsename = models.CharField(db_column='GrResponseName', max_length=100, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'eventservice20260101'


class Eventservice20260201(models.Model):
    service_id = models.AutoField(db_column='Service_id', primary_key=True)  # Field name made lowercase.
    namestate = models.CharField(db_column='NameState', max_length=60, blank=True, null=True)  # Field name made lowercase.
    event = models.ForeignKey(Archive20260201, models.DO_NOTHING, db_column='Event_id')  # Field name made lowercase.
    computer = models.CharField(db_column='Computer', max_length=50)  # Field name made lowercase.
    operationtime = models.DateTimeField(db_column='OperationTime')  # Field name made lowercase.
    date_key = models.IntegerField(db_column='Date_Key')  # Field name made lowercase.
    personname = models.CharField(db_column='PersonName', max_length=200, blank=True, null=True)  # Field name made lowercase.
    grresponsename = models.CharField(db_column='GrResponseName', max_length=100, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'eventservice20260201'


class Eventservice20260301(models.Model):
    service_id = models.AutoField(db_column='Service_id', primary_key=True)  # Field name made lowercase.
    namestate = models.CharField(db_column='NameState', max_length=60, blank=True, null=True)  # Field name made lowercase.
    event = models.ForeignKey(Archive20260301, models.DO_NOTHING, db_column='Event_id')  # Field name made lowercase.
    computer = models.CharField(db_column='Computer', max_length=50)  # Field name made lowercase.
    operationtime = models.DateTimeField(db_column='OperationTime')  # Field name made lowercase.
    date_key = models.IntegerField(db_column='Date_Key')  # Field name made lowercase.
    personname = models.CharField(db_column='PersonName', max_length=200, blank=True, null=True)  # Field name made lowercase.
    grresponsename = models.CharField(db_column='GrResponseName', max_length=100, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'eventservice20260301'
