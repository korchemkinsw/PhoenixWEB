# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Additionalarchiveinfo(models.Model):
    archive_id = models.IntegerField(db_column='Archive_id', primary_key=True)  # Field name made lowercase.
    additionaltext = models.CharField(db_column='AdditionalText', max_length=500, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'AdditionalArchiveInfo'


class Additionalstandinfo(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    archiveid = models.IntegerField(db_column='ArchiveID')  # Field name made lowercase.
    group = models.IntegerField(db_column='Group')  # Field name made lowercase.
    zone = models.IntegerField(db_column='Zone', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'AdditionalStandInfo'


class Advancesearchtemplates(models.Model):
    id = models.AutoField()
    typeoptions = models.SmallIntegerField(db_column='TypeOptions', blank=True, null=True)  # Field name made lowercase.
    templatename = models.CharField(db_column='TemplateName', max_length=200)  # Field name made lowercase.
    sqlstring = models.CharField(db_column='SQLString', max_length=5000)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'AdvanceSearchTemplates'


class Alarmeventforcomputers(models.Model):
    event = models.OneToOneField('Temp', models.DO_NOTHING, db_column='Event_id', primary_key=True)  # Field name made lowercase. The composite primary key (Event_id, ComputerName) found, that is not supported. The first column is selected.
    computername = models.CharField(db_column='ComputerName', max_length=70)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'AlarmEventForComputers'
        unique_together = (('event', 'computername'),)


class Archiveadditioninfo(models.Model):
    archiveeventid = models.IntegerField(db_column='ArchiveEventID', primary_key=True)  # Field name made lowercase.
    info = models.CharField(max_length=200, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ArchiveAdditionInfo'


class Archivegroupresponse(models.Model):
    group_id = models.IntegerField(db_column='Group_id')  # Field name made lowercase.
    starttime = models.DateTimeField(db_column='StartTime', blank=True, null=True)  # Field name made lowercase.
    endtime = models.DateTimeField(db_column='EndTime', blank=True, null=True)  # Field name made lowercase.
    status_id = models.IntegerField(db_column='Status_id', blank=True, null=True)  # Field name made lowercase.
    panel_id = models.CharField(db_column='Panel_id', max_length=15, blank=True, null=True)  # Field name made lowercase.
    group_field = models.IntegerField(db_column='Group_', blank=True, null=True)  # Field name made lowercase. Field renamed because it ended with '_'.

    class Meta:
        managed = False
        db_table = 'ArchiveGroupResponse'


class Archiveid(models.Model):
    current_id = models.IntegerField(db_column='Current_ID')  # Field name made lowercase.
    currentpictureid = models.IntegerField(db_column='CurrentPictureID')  # Field name made lowercase.
    currentgpsid = models.IntegerField(db_column='CurrentGPSID')  # Field name made lowercase.
    error_base_jurnal = models.IntegerField(db_column='Error_Base_Jurnal')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ArchiveID'


class Areas(models.Model):
    area_id = models.AutoField(db_column='Area_id', primary_key=True, db_comment='ID')  # Field name made lowercase.
    area_name = models.CharField(db_column='Area_name', unique=True, max_length=200, blank=True, null=True, db_comment='Название района')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Areas'
        db_table_comment = 'Районы'


class Auditgeozone(models.Model):
    geozone_id = models.IntegerField(db_column='GeoZone_Id')  # Field name made lowercase.
    actiontype = models.CharField(db_column='ActionType', max_length=3)  # Field name made lowercase.
    actiondate = models.DateTimeField(db_column='ActionDate')  # Field name made lowercase.
    actionuser = models.CharField(db_column='ActionUser', max_length=20)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'AuditGeoZone'


class Auditrunning(models.Model):
    computer = models.CharField(db_column='Computer', max_length=50, blank=True, null=True)  # Field name made lowercase.
    programtitle = models.CharField(db_column='ProgramTitle', max_length=100, blank=True, null=True)  # Field name made lowercase.
    runtime = models.DateTimeField(db_column='RunTime', blank=True, null=True)  # Field name made lowercase.
    runorclose = models.CharField(db_column='RunOrClose', max_length=10, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'AuditRunning'


class Availablestates(models.Model):
    state_id = models.IntegerField(db_column='State_id', db_comment='Текущее состояние события (Sta')  # Field name made lowercase.
    availablestate_id = models.IntegerField(db_column='AvailableState_id', db_comment='Допустимое состояние события п')  # Field name made lowercase.
    idtcode = models.ForeignKey('Typecode', models.DO_NOTHING, db_column='idTCode', blank=True, null=True, db_comment='TypeCode.idTCode')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'AvailableStates'
        db_table_comment = 'Допустимые изменения состояния'


class Central(models.Model):
    panel = models.OneToOneField('Panel', models.DO_NOTHING, primary_key=True, db_comment='Panel.Panel_id')
    central_id = models.CharField(db_column='Central_id', unique=True, max_length=15, db_comment='Передаваемый номер')  # Field name made lowercase.
    device = models.ForeignKey('Typedevices', models.DO_NOTHING, db_column='Device_id', blank=True, null=True, db_comment='TypeDevices.Device_id')  # Field name made lowercase.
    phonenumber = models.CharField(db_column='PhoneNumber', max_length=15, blank=True, null=True, db_comment='Номер телефона')  # Field name made lowercase.
    mainpower = models.BooleanField(db_column='MainPower', blank=True, null=True, db_comment='Основное питание: 1 - есть; 0 ')  # Field name made lowercase.
    backuppower = models.BooleanField(db_column='BackupPower', blank=True, null=True, db_comment='Резервное питание: 1 - есть; 0')  # Field name made lowercase.
    mptime = models.DateTimeField(db_column='MPTime', blank=True, null=True, db_comment='Время последнего изменения сос')  # Field name made lowercase.
    bptime = models.DateTimeField(db_column='BPTime', blank=True, null=True, db_comment='Время последнего изменения сос')  # Field name made lowercase.
    lasttest = models.DateTimeField(db_column='LastTest', blank=True, null=True, db_comment='Время последнего теста')  # Field name made lowercase.
    testtimeout = models.DateTimeField(db_column='TestTimeout', blank=True, null=True, db_comment='Период тестирования')  # Field name made lowercase.
    codegroup = models.IntegerField(db_column='CodeGroup', blank=True, null=True, db_comment='Набор кодов')  # Field name made lowercase.
    typetest = models.IntegerField(db_column='typeTest', blank=True, null=True, db_comment='Тип тестирования: 0 - 1 раз в ')  # Field name made lowercase.
    statusz1 = models.BooleanField(db_column='StatusZ1', blank=True, null=True, db_comment='Был ли сгенерирован код Z1: 1 ')  # Field name made lowercase.
    npack = models.IntegerField(db_column='Npack', blank=True, null=True, db_comment='Номер пакета от прибора (тольк')  # Field name made lowercase.
    alarmdelay = models.IntegerField(db_column='AlarmDelay', blank=True, null=True)  # Field name made lowercase.
    lastopenalarmtime = models.DateTimeField(db_column='LastOpenAlarmTime', blank=True, null=True)  # Field name made lowercase.
    alarmcode = models.CharField(db_column='AlarmCode', max_length=10, blank=True, null=True)  # Field name made lowercase.
    testtimeoutclose = models.DateTimeField(db_column='TestTimeOutClose', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Central'
        db_table_comment = 'ППК'


class Centralalarmsdelaylist(models.Model):
    panel_id = models.CharField(max_length=15)
    group = models.IntegerField()
    alarmcode = models.CharField(db_column='AlarmCode', max_length=10)  # Field name made lowercase.
    alarmtime = models.DateTimeField(db_column='AlarmTime')  # Field name made lowercase.
    alarmzone = models.IntegerField(db_column='AlarmZone', blank=True, null=True)  # Field name made lowercase.
    alarmcodegroup = models.IntegerField(db_column='AlarmCodeGroup')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CentralAlarmsDelayList'


class ChangedataLog(models.Model):
    operation = models.SmallIntegerField()
    object = models.CharField(max_length=200, blank=True, null=True)
    panel_id = models.CharField(max_length=200, blank=True, null=True)
    group_field = models.IntegerField(db_column='Group_', blank=True, null=True)  # Field name made lowercase. Field renamed because it ended with '_'.
    table_name = models.CharField(db_column='Table_Name', max_length=200)  # Field name made lowercase.
    table_field = models.ForeignKey('Fielddictionary', models.DO_NOTHING, db_column='Table_Field')  # Field name made lowercase.
    valuebefore = models.CharField(db_column='ValueBefore', max_length=3000)  # Field name made lowercase.
    valueafter = models.CharField(db_column='ValueAfter', max_length=3000)  # Field name made lowercase.
    operation_date = models.DateTimeField(db_column='Operation_Date')  # Field name made lowercase.
    username = models.CharField(db_column='UserName', max_length=200)  # Field name made lowercase.
    computer = models.CharField(db_column='Computer', max_length=15)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ChangeData_Log'


class Channeltypes(models.Model):
    channeltype_id = models.AutoField(db_column='ChannelType_id', primary_key=True, db_comment='ID')  # Field name made lowercase.
    channeltype = models.CharField(db_column='ChannelType', unique=True, max_length=100, blank=True, null=True, db_comment='Режим работы прибора')  # Field name made lowercase.
    priority = models.IntegerField(blank=True, null=True, db_comment='Приоритет')

    class Meta:
        managed = False
        db_table = 'ChannelTypes'
        db_table_comment = 'Типы каналов'


class Channels(models.Model):
    sim = models.ForeignKey('Sims', models.DO_NOTHING, db_column='SIM_id', blank=True, null=True, db_comment='Sims.SIM_id')  # Field name made lowercase.
    channeltype = models.ForeignKey(Channeltypes, models.DO_NOTHING, db_column='ChannelType_id', blank=True, null=True, db_comment='ChannelTypes.ChannelType_id')  # Field name made lowercase.
    testtimeout = models.DateTimeField(db_column='TestTimeout', blank=True, null=True, db_comment='Период тестирования')  # Field name made lowercase.
    lasttestchannel = models.DateTimeField(db_column='LastTestChannel', blank=True, null=True, db_comment='Дата и время последнего теста ')  # Field name made lowercase.
    statusz222 = models.BooleanField(db_column='StatusZ222', blank=True, null=True, db_comment='Был ли сгенерирован код Z222: ')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Channels'
        db_table_comment = 'Режимы работы приборов'


class ChannelsChannelno(models.Model):
    channel = models.OneToOneField(Channels, models.DO_NOTHING)
    channelno = models.CharField(db_column='ChannelNo', primary_key=True, max_length=15)  # Field name made lowercase. The composite primary key (ChannelNo, VPN_id) found, that is not supported. The first column is selected.
    channelnoforstate = models.CharField(db_column='ChannelNoForState', max_length=15)  # Field name made lowercase.
    vpn_id = models.IntegerField(db_column='VPN_id')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Channels_ChannelNo'
        unique_together = (('channelno', 'vpn_id'), ('channelnoforstate', 'vpn_id'),)


class Clientdata(models.Model):
    companyname = models.CharField(db_column='CompanyName', max_length=1000)  # Field name made lowercase.
    country = models.CharField(db_column='Country', max_length=100)  # Field name made lowercase.
    city = models.CharField(db_column='City', max_length=100)  # Field name made lowercase.
    address = models.CharField(max_length=100)
    fio = models.CharField(db_column='FIO', max_length=100)  # Field name made lowercase.
    telephone = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    othercontacts = models.CharField(db_column='otherContacts', max_length=100, blank=True, null=True)  # Field name made lowercase.
    regkey = models.CharField(db_column='RegKey', max_length=100, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ClientData'


class Clientsettings(models.Model):
    computername = models.CharField(db_column='ComputerName', max_length=70)  # Field name made lowercase.
    idtcode = models.IntegerField(db_column='IdTCode', primary_key=True)  # Field name made lowercase. The composite primary key (IdTCode, ComputerName) found, that is not supported. The first column is selected.

    class Meta:
        managed = False
        db_table = 'ClientSettings'
        unique_together = (('idtcode', 'computername'),)


class Code(models.Model):
    code = models.CharField(db_column='Code', primary_key=True, max_length=6)  # Field name made lowercase. The composite primary key (Code, CodeGroup) found, that is not supported. The first column is selected.
    codegroup = models.SmallIntegerField(db_column='CodeGroup')  # Field name made lowercase.
    message = models.CharField(db_column='Message', max_length=500, blank=True, null=True)  # Field name made lowercase.
    autoreset = models.BooleanField(db_column='AutoReset', blank=True, null=True)  # Field name made lowercase.
    groupsent = models.BooleanField(db_column='GroupSent', blank=True, null=True)  # Field name made lowercase.
    flag = models.IntegerField(db_column='Flag', blank=True, null=True)  # Field name made lowercase.
    zoneno = models.IntegerField(db_column='Zoneno', blank=True, null=True)  # Field name made lowercase.
    svet = models.SmallIntegerField(db_column='Svet', blank=True, null=True)  # Field name made lowercase.
    accesscode = models.BooleanField(db_column='AccessCode', blank=True, null=True)  # Field name made lowercase.
    filename = models.CharField(db_column='FileName', max_length=100, blank=True, null=True)  # Field name made lowercase.
    idtcode = models.ForeignKey('Typecode', models.DO_NOTHING, db_column='idTCode', blank=True, null=True)  # Field name made lowercase.
    system = models.BooleanField(db_column='System', blank=True, null=True)  # Field name made lowercase.
    isneedreport = models.BooleanField(db_column='IsNeedReport', blank=True, null=True)  # Field name made lowercase.
    contactid_code = models.CharField(db_column='contactId_code', max_length=4, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Code'
        unique_together = (('code', 'codegroup'),)


class Company(models.Model):
    companyname = models.CharField(db_column='CompanyName', max_length=150, blank=True, null=True, db_comment='Название')  # Field name made lowercase.
    address = models.CharField(max_length=150, blank=True, null=True, db_comment='Адрес')
    telephones = models.CharField(db_column='Telephones', max_length=100, blank=True, null=True, db_comment='Телефоны')  # Field name made lowercase.
    director = models.CharField(db_column='Director', max_length=150, blank=True, null=True, db_comment='Директор')  # Field name made lowercase.
    director2 = models.CharField(db_column='Director2', max_length=150, blank=True, null=True, db_comment='Ответственный')  # Field name made lowercase.
    computer = models.CharField(db_column='Computer', max_length=100, blank=True, null=True, db_comment='Имя компьютера, на котором изм')  # Field name made lowercase.
    memo = models.CharField(db_column='Memo', max_length=7000, blank=True, null=True, db_comment='Дополнительная информация')  # Field name made lowercase.
    lasteditdate = models.DateTimeField(db_column='LastEditDate', blank=True, null=True, db_comment='Дата последнего изменения запи')  # Field name made lowercase.
    company_id = models.CharField(primary_key=True, max_length=18, db_comment='ID')
    username = models.CharField(db_column='UserName', max_length=200, blank=True, null=True, db_comment='Имя пользователя, который изме')  # Field name made lowercase.
    serviceid = models.ForeignKey('Serviceorganization', models.DO_NOTHING, db_column='ServiceID', blank=True, null=True, db_comment='ServiceOrganization.ID')  # Field name made lowercase.
    customerid = models.ForeignKey('Customers', models.DO_NOTHING, db_column='CustomerID', blank=True, null=True, db_comment='Customers.ID')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Company'
        db_table_comment = 'Плательщик'


class CompanyContracts(models.Model):
    contract = models.OneToOneField('Contracts', models.DO_NOTHING, db_column='Contract_id', primary_key=True, db_comment='Contracts.Contract_id')  # Field name made lowercase. The composite primary key (Contract_id, company_id) found, that is not supported. The first column is selected.
    contractrent = models.CharField(db_column='ContractRent', max_length=500, blank=True, null=True, db_comment='Оборудование в аренде')  # Field name made lowercase.
    company = models.ForeignKey(Company, models.DO_NOTHING, db_comment='Company.company_id')
    remarks = models.CharField(db_column='Remarks', max_length=1000, blank=True, null=True, db_comment='Примечания')  # Field name made lowercase.
    doc = models.BooleanField(db_column='Doc')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Company_Contracts'
        unique_together = (('contract', 'company'),)


class Contactidemulationchanneltype(models.Model):
    id = models.IntegerField(db_column='ID', primary_key=True)  # Field name made lowercase.
    channeltype = models.CharField(db_column='ChannelType', unique=True, max_length=50)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ContactIDEmulationChannelType'


class Contactidemulationsetting(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    channeltype = models.ForeignKey(Contactidemulationchanneltype, models.DO_NOTHING, db_column='ChannelType_ID')  # Field name made lowercase.
    eventsourcename = models.CharField(db_column='EventSourceName', max_length=50)  # Field name made lowercase.
    ip = models.CharField(db_column='IP', max_length=15, blank=True, null=True)  # Field name made lowercase.
    port = models.CharField(db_column='Port', max_length=6, blank=True, null=True)  # Field name made lowercase.
    comport = models.CharField(db_column='COMPort', max_length=50, blank=True, null=True)  # Field name made lowercase.
    com_speed = models.IntegerField(db_column='COM_Speed', blank=True, null=True)  # Field name made lowercase.
    com_byte_size = models.SmallIntegerField(db_column='COM_Byte_size', blank=True, null=True)  # Field name made lowercase.
    com_parity = models.SmallIntegerField(db_column='COM_Parity', blank=True, null=True)  # Field name made lowercase.
    com_stop_bit = models.CharField(db_column='COM_Stop_bit', max_length=10, blank=True, null=True)  # Field name made lowercase.
    computername = models.CharField(db_column='ComputerName', max_length=50, blank=True, null=True)  # Field name made lowercase.
    switchon = models.BooleanField(db_column='SwitchOn')  # Field name made lowercase.
    isincludeddatetime = models.BooleanField(db_column='IsIncludedDateTime')  # Field name made lowercase.
    isusefiltersbypults = models.BooleanField(db_column='IsUseFiltersByPults')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ContactIDEmulationSetting'


class Contactideventsfilterbypults(models.Model):
    id = models.AutoField(db_column='ID')  # Field name made lowercase.
    contactidsettingid = models.OneToOneField(Contactidemulationsetting, models.DO_NOTHING, db_column='ContactIDSettingID', primary_key=True)  # Field name made lowercase. The composite primary key (ContactIDSettingID, PultID) found, that is not supported. The first column is selected.
    pultid = models.ForeignKey('Pults', models.DO_NOTHING, db_column='PultID')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ContactIDEventsFilterByPults'
        unique_together = (('contactidsettingid', 'pultid'),)


class Contactidphoenixcodes(models.Model):
    id = models.AutoField(db_column='ID')  # Field name made lowercase.
    contactidcode = models.CharField(db_column='ContactIDCode', max_length=255, blank=True, null=True)  # Field name made lowercase.
    description = models.CharField(db_column='Description', max_length=255, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ContactIDPhoenixCodes'


class Contactidviacomevents(models.Model):
    id = models.AutoField(db_column='ID')  # Field name made lowercase.
    eventid = models.IntegerField(db_column='EventID', primary_key=True)  # Field name made lowercase. The composite primary key (EventID, ComputerName, COMPort) found, that is not supported. The first column is selected.
    contactidpacket = models.CharField(db_column='ContactIDPacket', max_length=7000)  # Field name made lowercase.
    computername = models.CharField(db_column='ComputerName', max_length=50)  # Field name made lowercase.
    comport = models.CharField(db_column='COMPort', max_length=50)  # Field name made lowercase.
    sendstatus = models.IntegerField(db_column='SendStatus')  # Field name made lowercase.
    eventdate = models.DateTimeField(db_column='EventDate')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ContactIDViaCOMEvents'
        unique_together = (('eventid', 'computername', 'comport'),)


class Contactidviatcpevents(models.Model):
    id = models.AutoField(db_column='ID')  # Field name made lowercase.
    eventid = models.IntegerField(db_column='EventID', primary_key=True)  # Field name made lowercase. The composite primary key (EventID, ComputerName, IP, Port) found, that is not supported. The first column is selected.
    contactidpacket = models.CharField(db_column='ContactIDPacket', max_length=7000)  # Field name made lowercase.
    computername = models.CharField(db_column='ComputerName', max_length=50)  # Field name made lowercase.
    ip = models.CharField(db_column='IP', max_length=50)  # Field name made lowercase.
    port = models.CharField(db_column='Port', max_length=50)  # Field name made lowercase.
    sendstatus = models.IntegerField(db_column='SendStatus')  # Field name made lowercase.
    eventdate = models.DateTimeField(db_column='EventDate')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ContactIDViaTCPEvents'
        unique_together = (('eventid', 'computername', 'ip', 'port'),)


class Contracts(models.Model):
    contract_id = models.CharField(db_column='Contract_id', primary_key=True, max_length=25, db_comment='ID')  # Field name made lowercase.
    contractdate = models.DateTimeField(db_column='ContractDate', blank=True, null=True, db_comment='Начальная дата')  # Field name made lowercase.
    firm = models.ForeignKey('Firms', models.DO_NOTHING, db_column='Firm_id', blank=True, null=True, db_comment='Firms.Firm_id')  # Field name made lowercase.
    contractdateto = models.DateTimeField(db_column='ContractDateTo', blank=True, null=True, db_comment='Конечная дата')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Contracts'
        db_table_comment = 'Договора'


class Currentalarms(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    recipient_channelno = models.CharField(db_column='Recipient_ChannelNo', max_length=50, blank=True, null=True)  # Field name made lowercase.
    recipient_type = models.SmallIntegerField(db_column='Recipient_Type', blank=True, null=True)  # Field name made lowercase.
    panel_id = models.CharField(db_column='Panel_id', max_length=15)  # Field name made lowercase.
    group_field = models.IntegerField(db_column='Group_')  # Field name made lowercase. Field renamed because it ended with '_'.
    zone = models.IntegerField(db_column='Zone')  # Field name made lowercase.
    code = models.CharField(db_column='Code', max_length=6)  # Field name made lowercase.
    codegroup = models.SmallIntegerField(db_column='CodeGroup')  # Field name made lowercase.
    timeevent = models.DateTimeField(db_column='TimeEvent')  # Field name made lowercase.
    timesendevent = models.DateTimeField(db_column='TimeSendEvent', blank=True, null=True)  # Field name made lowercase.
    timeacceptevent = models.DateTimeField(db_column='TimeAcceptEvent', blank=True, null=True)  # Field name made lowercase.
    metercount = models.CharField(db_column='MeterCount', max_length=50, blank=True, null=True)  # Field name made lowercase.
    result = models.SmallIntegerField(db_column='Result', blank=True, null=True)  # Field name made lowercase.
    ncds_sms = models.IntegerField(db_column='NCDS_SMS', blank=True, null=True)  # Field name made lowercase.
    text = models.CharField(db_column='Text', max_length=1000, blank=True, null=True)  # Field name made lowercase.
    computername = models.CharField(db_column='ComputerName', max_length=70, blank=True, null=True)  # Field name made lowercase.
    timeputwebserverevent = models.DateTimeField(db_column='TimePutWebServerEvent', blank=True, null=True)  # Field name made lowercase.
    timesendafter = models.DateTimeField(db_column='TimeSendAfter', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CurrentAlarms'


class Currentconnection(models.Model):
    computername = models.CharField(db_column='ComputerName', primary_key=True, max_length=50)  # Field name made lowercase.
    send = models.BooleanField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'CurrentConnection'


class Customers(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    organization = models.CharField(db_column='Organization', max_length=500, blank=True, null=True)  # Field name made lowercase.
    organizationaddress = models.CharField(db_column='OrganizationAddress', max_length=500, blank=True, null=True)  # Field name made lowercase.
    director = models.CharField(db_column='Director', max_length=500, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Customers'


class Databaseversion(models.Model):
    version = models.IntegerField(primary_key=True)  # The composite primary key (version, versionDate) found, that is not supported. The first column is selected.
    versiondate = models.DateTimeField(db_column='versionDate')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DataBaseVersion'
        unique_together = (('version', 'versiondate'),)


class DeviceModification(models.Model):
    id = models.OneToOneField('self', models.DO_NOTHING, db_column='id', primary_key=True)
    device_id = models.SmallIntegerField(db_column='Device_id')  # Field name made lowercase.
    modifications = models.CharField(db_column='Modifications', max_length=50)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Device_Modification'
        unique_together = (('device_id', 'modifications'),)


class Dictentattrval(models.Model):
    dictid = models.AutoField(db_column='DictID', primary_key=True)  # Field name made lowercase.
    dictlevel = models.ForeignKey('self', models.DO_NOTHING, db_column='DictLevel', blank=True, null=True)  # Field name made lowercase.
    dictparentid = models.ForeignKey('self', models.DO_NOTHING, db_column='DictParentID', related_name='dictentattrval_dictparentid_set', blank=True, null=True)  # Field name made lowercase.
    dictvalue = models.CharField(db_column='DictValue', max_length=50)  # Field name made lowercase.
    dictdescription = models.CharField(db_column='DictDescription', max_length=4000, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DictEntAttrVal'
        unique_together = (('dictlevel', 'dictparentid', 'dictvalue'),)


class Engineersphmk(models.Model):
    engineer = models.OneToOneField('Engineers', models.DO_NOTHING, primary_key=True)  # The composite primary key (engineer_id, userGrId) found, that is not supported. The first column is selected.
    usergrid = models.ForeignKey('MobileuserGroups', models.DO_NOTHING, db_column='userGrId', to_field='userGrId')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'EngineersPhMk'
        unique_together = (('engineer', 'usergrid'),)


class Eventsrecipients(models.Model):
    recipient_id = models.AutoField(db_column='Recipient_id', primary_key=True, db_comment='ID')  # Field name made lowercase.
    recipientiporphone = models.CharField(db_column='RecipientIPorPhone', max_length=15, blank=True, null=True, db_comment='Номер телефона или IP адрес')  # Field name made lowercase.
    orlanpairnumber = models.SmallIntegerField(db_column='OrlanPairNumber', blank=True, null=True, db_comment='Номер пары GPRS Орланов, с кот')  # Field name made lowercase.
    responsibletel = models.ForeignKey('Responsibletel', models.DO_NOTHING, db_column='ResponsibleTel_id', blank=True, null=True)  # Field name made lowercase.
    responsibleemail = models.ForeignKey('Responsibleemail', models.DO_NOTHING, db_column='ResponsibleEmail_id', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'EventsRecipients'
        unique_together = (('recipientiporphone', 'responsibletel', 'responsibleemail'),)
        db_table_comment = 'Получатели сообщений'


class Eventssendlog(models.Model):
    log_id = models.AutoField(primary_key=True)
    logtype_id = models.IntegerField(db_column='LogType_id')  # Field name made lowercase.
    panel_id = models.CharField(db_column='Panel_id', max_length=15, blank=True, null=True)  # Field name made lowercase.
    group_field = models.IntegerField(db_column='Group_', blank=True, null=True)  # Field name made lowercase. Field renamed because it ended with '_'.
    zone = models.IntegerField(db_column='Zone', blank=True, null=True)  # Field name made lowercase.
    code = models.CharField(db_column='Code', max_length=6, blank=True, null=True)  # Field name made lowercase.
    codegroup = models.IntegerField(db_column='CodeGroup', blank=True, null=True)  # Field name made lowercase.
    datetimesend = models.DateTimeField(db_column='DateTimeSend', blank=True, null=True)  # Field name made lowercase.
    datetimerecived = models.DateTimeField(db_column='DateTimeRecived', blank=True, null=True)  # Field name made lowercase.
    result = models.SmallIntegerField(blank=True, null=True)
    metercount = models.CharField(db_column='MeterCount', max_length=50, blank=True, null=True)  # Field name made lowercase.
    textsms = models.CharField(db_column='TextSMS', max_length=1000, blank=True, null=True)  # Field name made lowercase.
    addressremotepult = models.CharField(db_column='AddressRemotePult', max_length=15, blank=True, null=True)  # Field name made lowercase.
    timeputwebserverevent = models.DateTimeField(db_column='TimePutWebServerEvent', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'EventsSendLog'


class Extensiontypes(models.Model):
    extype_id = models.AutoField(db_column='ExType_id', primary_key=True, db_comment='ID')  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=20, db_comment='Name of extensions device')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ExtensionTypes'


class Fielddictionary(models.Model):
    dbname = models.CharField(db_column='DBName', unique=True, max_length=200)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=200)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'FieldDictionary'


class Firms(models.Model):
    firm_id = models.AutoField(db_column='Firm_id', primary_key=True, db_comment='ID')  # Field name made lowercase.
    firm_name = models.CharField(unique=True, max_length=200, db_comment='Юридическое лицо')

    class Meta:
        managed = False
        db_table = 'Firms'
        db_table_comment = 'Юридическиее лица'


class Gprsrequest(models.Model):
    request_id = models.AutoField(db_column='Request_id', primary_key=True)  # Field name made lowercase.
    ip = models.CharField(db_column='IP', max_length=15)  # Field name made lowercase.
    orlanpair = models.SmallIntegerField(db_column='OrlanPair', blank=True, null=True)  # Field name made lowercase.
    request_type = models.SmallIntegerField(db_column='Request_type')  # Field name made lowercase.
    zone = models.IntegerField(db_column='Zone', blank=True, null=True)  # Field name made lowercase.
    deviceid = models.SmallIntegerField(db_column='DeviceID', blank=True, null=True)  # Field name made lowercase.
    timeforcommand = models.DateTimeField(db_column='TimeForCommand', blank=True, null=True)  # Field name made lowercase.
    panel_id = models.CharField(db_column='Panel_id', max_length=15, blank=True, null=True)  # Field name made lowercase.
    group_field = models.IntegerField(db_column='Group_', blank=True, null=True)  # Field name made lowercase. Field renamed because it ended with '_'.
    openinternetnumber = models.IntegerField(db_column='OpenInternetNumber', blank=True, null=True)  # Field name made lowercase.
    vpn_id = models.IntegerField(db_column='VPN_id', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'GPRSRequest'


class Gpscurrentconvertdate(models.Model):
    currentvalue = models.DateTimeField(db_column='currentValue', blank=True, null=True)  # Field name made lowercase.
    type = models.CharField(max_length=2, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'GPSCurrentConvertDate'


class Gpsobjectdata(models.Model):
    tableid = models.CharField(db_column='TableID', primary_key=True, max_length=15)  # Field name made lowercase.
    name = models.CharField(max_length=150, blank=True, null=True)
    description = models.CharField(db_column='Description', max_length=350, blank=True, null=True)  # Field name made lowercase.
    longtitude = models.CharField(db_column='Longtitude', max_length=15, blank=True, null=True)  # Field name made lowercase.
    latitude = models.CharField(db_column='Latitude', max_length=15, blank=True, null=True)  # Field name made lowercase.
    category = models.CharField(max_length=3, blank=True, null=True)
    engine = models.BooleanField(blank=True, null=True)
    panel_id = models.CharField(max_length=15, blank=True, null=True)
    statusz2 = models.BooleanField(db_column='StatusZ2', blank=True, null=True)  # Field name made lowercase.
    isgpsvalid = models.BooleanField(db_column='isGPSValid', blank=True, null=True)  # Field name made lowercase.
    powergps = models.BooleanField(db_column='PowerGPS', blank=True, null=True)  # Field name made lowercase.
    gpsarrivetime = models.DateTimeField(db_column='GPSArriveTime', blank=True, null=True)  # Field name made lowercase.
    reason = models.CharField(max_length=100, blank=True, null=True)
    group_id = models.IntegerField(blank=True, null=True)
    status_id = models.IntegerField(blank=True, null=True)
    courseoverground = models.CharField(db_column='CourseOverGround', max_length=10, blank=True, null=True)  # Field name made lowercase.
    address = models.CharField(max_length=150, blank=True, null=True)
    director = models.CharField(max_length=150, blank=True, null=True)
    director2 = models.CharField(max_length=150, blank=True, null=True)
    memo = models.CharField(max_length=6000, blank=True, null=True)
    telephones = models.CharField(max_length=100, blank=True, null=True)
    isalarm = models.BooleanField(db_column='isAlarm', blank=True, null=True)  # Field name made lowercase.
    alarmtime = models.DateTimeField(db_column='AlarmTime', blank=True, null=True)  # Field name made lowercase.
    mainpower = models.BooleanField(db_column='MainPower', blank=True, null=True)  # Field name made lowercase.
    backuppower = models.BooleanField(db_column='BackUpPower', blank=True, null=True)  # Field name made lowercase.
    currentchannel = models.CharField(db_column='CurrentChannel', max_length=100, blank=True, null=True)  # Field name made lowercase.
    isopen = models.BooleanField(db_column='isOpen', blank=True, null=True)  # Field name made lowercase.
    coordstatus = models.CharField(db_column='CoordStatus', max_length=1, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'GPSObjectData'


class Geozone(models.Model):
    name = models.CharField(db_column='Name', max_length=300)  # Field name made lowercase.
    description = models.CharField(db_column='Description', max_length=300)  # Field name made lowercase.
    zonetype = models.ForeignKey('Geozonetype', models.DO_NOTHING, db_column='ZoneType')  # Field name made lowercase.
    base64points = models.CharField(db_column='Base64Points', max_length=8000)  # Field name made lowercase.
    points = models.CharField(db_column='Points', max_length=8000)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'GeoZone'


class Geozonetype(models.Model):
    description = models.CharField(db_column='Description', max_length=300)  # Field name made lowercase.
    color = models.CharField(db_column='Color', max_length=8)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'GeoZoneType'


class Groupresponse(models.Model):
    group_id = models.IntegerField(db_column='Group_id', primary_key=True, db_comment='ID')  # Field name made lowercase.
    description = models.CharField(db_column='Description', max_length=100, blank=True, null=True, db_comment='Название')  # Field name made lowercase.
    starttime = models.DateTimeField(db_column='StartTime', blank=True, null=True, db_comment='Начало работы')  # Field name made lowercase.
    endtime = models.DateTimeField(db_column='EndTime', blank=True, null=True, db_comment='Конец работы')  # Field name made lowercase.
    status = models.ForeignKey('Statusgroupresponse', models.DO_NOTHING, db_column='Status_id', db_comment='StatusGroupResponse.status_id')  # Field name made lowercase.
    event_id = models.IntegerField(db_column='Event_id', blank=True, null=True, db_comment='Текущее событие, пришедшее от ')  # Field name made lowercase.
    panel_id = models.CharField(db_column='Panel_id', max_length=15, blank=True, null=True, db_comment='Groups.Panel_id')  # Field name made lowercase.
    group_field = models.IntegerField(db_column='Group_', blank=True, null=True, db_comment='Groups.Group_')  # Field name made lowercase. Field renamed because it ended with '_'.
    engine = models.BooleanField(db_column='Engine', db_comment='Зажигание включено: 1 - да; 0 ')  # Field name made lowercase.
    track = models.IntegerField(db_column='Track', db_comment='ID трека (FK на базу данных GP')  # Field name made lowercase.
    mphone = models.ForeignKey('Mphone', models.DO_NOTHING, db_column='Mphone_id', blank=True, null=True, db_comment='MPhone.Mphone_id')  # Field name made lowercase.
    lastgpsidfrommobile = models.IntegerField(db_column='LastGPSIdFromMobile', blank=True, null=True, db_comment='Координаты от Киевстара (не ис')  # Field name made lowercase.
    disabled = models.BooleanField(db_column='Disabled', db_comment='Прибор отключен: 1 - да; 0 - н')  # Field name made lowercase.
    category = models.ForeignKey('Groupresponsecategory', models.DO_NOTHING, db_column='Category', blank=True, null=True, db_comment='GroupResponseCategory.Category')  # Field name made lowercase.
    callsign = models.CharField(max_length=50, blank=True, null=True, db_comment='Позывной группы')
    geozone_id = models.IntegerField(db_column='GeoZone_id', db_comment='Не используется')  # Field name made lowercase.
    dislocationpointlat = models.CharField(db_column='DislocationPointLat', max_length=15, db_comment='Широта точки дислокации группы')  # Field name made lowercase.
    dislocationpointlon = models.CharField(db_column='DislocationPointLon', max_length=15, db_comment='Долгота точки дислокации групп')  # Field name made lowercase.
    timearrivetoobject = models.DateTimeField(db_column='TimeArriveToObject', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'GroupResponse'
        unique_together = (('category', 'description'),)
        db_table_comment = 'Группы реагирования'


class Groupresponsealter(models.Model):
    groupresponse_id = models.IntegerField(db_column='GroupResponse_id', primary_key=True)  # Field name made lowercase. The composite primary key (GroupResponse_id, GroupResponseAlter_id) found, that is not supported. The first column is selected.
    groupresponsealter_id = models.IntegerField(db_column='GroupResponseAlter_id')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'GroupResponseAlter'
        unique_together = (('groupresponse_id', 'groupresponsealter_id'),)


class Groupresponsecategory(models.Model):
    categoryid = models.AutoField(db_column='CategoryID', primary_key=True)  # Field name made lowercase.
    description = models.CharField(db_column='Description', unique=True, max_length=100, blank=True, null=True)  # Field name made lowercase.
    sendidcategory = models.IntegerField(db_column='SendIdCategory', unique=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'GroupResponseCategory'


class Groupresponsegpsdatafrommobile(models.Model):
    id = models.IntegerField(unique=True)
    group_id = models.IntegerField(db_column='Group_id', blank=True, null=True)  # Field name made lowercase.
    coordx = models.CharField(db_column='CoordX', max_length=12, blank=True, null=True)  # Field name made lowercase.
    coordy = models.CharField(db_column='CoordY', max_length=12, blank=True, null=True)  # Field name made lowercase.
    startangle = models.CharField(db_column='StartAngle', max_length=4, blank=True, null=True)  # Field name made lowercase.
    stopangle = models.CharField(db_column='StopAngle', max_length=3, blank=True, null=True)  # Field name made lowercase.
    inradius = models.CharField(db_column='InRadius', max_length=4, blank=True, null=True)  # Field name made lowercase.
    outradius = models.CharField(db_column='OutRadius', max_length=8, blank=True, null=True)  # Field name made lowercase.
    timereceived = models.DateTimeField(db_column='TimeReceived', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'GroupResponseGPSDataFromMobile'


class Groupresponsegeozone(models.Model):
    group = models.ForeignKey(Groupresponse, models.DO_NOTHING, db_column='Group_id')  # Field name made lowercase.
    geozone = models.ForeignKey(Geozone, models.DO_NOTHING, db_column='GeoZone_id')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'GroupResponseGeoZone'


class GroupresponseGroup(models.Model):
    id = models.AutoField(db_comment='ID')
    group_id = models.IntegerField(db_column='Group_id', primary_key=True, db_comment='GroupResponse.Group_id')  # Field name made lowercase. The composite primary key (Group_id, Panel_id, group_) found, that is not supported. The first column is selected.
    panel = models.ForeignKey('Groups', models.DO_NOTHING, db_column='Panel_id', db_comment='Groups.Panel_id')  # Field name made lowercase.
    group_field = models.ForeignKey('Groups', models.DO_NOTHING, db_column='group_', related_name='groupresponsegroup_group_field_set', db_comment='Groups.Group_')  # Field renamed because it ended with '_'.
    starttime = models.DateTimeField(db_column='StartTime', blank=True, null=True, db_comment='Начало работы')  # Field name made lowercase.
    endtime = models.DateTimeField(db_column='EndTime', blank=True, null=True, db_comment='Конец работы')  # Field name made lowercase.
    maingroup = models.BooleanField(db_column='MainGroup', blank=True, null=True, db_comment='1 - Основная; 0 - Резервная')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'GroupResponse_Group'
        unique_together = (('group_id', 'panel', 'group_field'),)
        db_table_comment = 'Группы реагирования для выезда'


class GroupresponsePanel(models.Model):
    group_id = models.IntegerField(db_column='Group_id')  # Field name made lowercase.
    panel_id = models.CharField(db_column='Panel_id', max_length=15)  # Field name made lowercase.
    starttime = models.DateTimeField(db_column='StartTime', blank=True, null=True)  # Field name made lowercase.
    endtime = models.DateTimeField(db_column='EndTime', blank=True, null=True)  # Field name made lowercase.
    maingroup = models.BooleanField(db_column='MainGroup', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'GroupResponse_Panel'


class GroupSmsCode(models.Model):
    panel = models.ForeignKey('Groups', models.DO_NOTHING, db_column='Panel_id', db_comment='Groups.Panel_id')  # Field name made lowercase.
    code = models.ForeignKey(Code, models.DO_NOTHING, db_column='Code', to_field='CodeGroup', db_comment='Code.Code')  # Field name made lowercase.
    codegroup = models.ForeignKey(Code, models.DO_NOTHING, db_column='CodeGroup', to_field='CodeGroup', related_name='groupsmscode_codegroup_set', db_comment='Code.CodeGroup')  # Field name made lowercase.
    group_field = models.ForeignKey('Groups', models.DO_NOTHING, db_column='Group_', related_name='groupsmscode_group_field_set', db_comment='Groups.Group_')  # Field name made lowercase. Field renamed because it ended with '_'.
    recipient = models.ForeignKey(Eventsrecipients, models.DO_NOTHING, db_column='Recipient_id', db_comment='EventsRecipients.Recipient_id')  # Field name made lowercase.
    typesentsms = models.BooleanField(db_column='typeSentSMS', blank=True, null=True, db_comment='Не используется')  # Field name made lowercase.
    typesms = models.BooleanField(db_column='typeSMS', blank=True, null=True, db_comment='0 - кодированное сообщение; 1 ')  # Field name made lowercase.
    recipient_type = models.SmallIntegerField(db_column='Recipient_type', blank=True, null=True, db_comment='Получатель: 1 - Хозяйственник;')  # Field name made lowercase.
    typeaddcodes = models.BooleanField(db_column='TypeAddCodes', blank=True, null=True, db_comment='0 - коды выбраны по типам кодо')  # Field name made lowercase.
    zoneid = models.IntegerField(db_column='ZoneID', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Group_SMS_Code'
        db_table_comment = 'Пересылаемые события'


class GroupSmsCodeZones(models.Model):
    zoneid = models.IntegerField(db_column='ZoneId')  # Field name made lowercase.
    zonenumber = models.IntegerField(db_column='ZoneNumber')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Group_SMS_Code_Zones'


class Groups(models.Model):
    panel = models.OneToOneField('Panel', models.DO_NOTHING, db_column='Panel_id', primary_key=True, db_comment='Panel.Panel_id')  # Field name made lowercase. The composite primary key (Panel_id, Group_) found, that is not supported. The first column is selected.
    group_field = models.IntegerField(db_column='Group_', db_comment='Номер')  # Field name made lowercase. Field renamed because it ended with '_'.
    message = models.CharField(db_column='Message', max_length=100, db_comment='Описание')  # Field name made lowercase.
    isopen = models.BooleanField(db_column='IsOpen', blank=True, null=True, db_comment='Группа под охраной: 0 - да; 1 ')  # Field name made lowercase.
    timeevent = models.DateTimeField(db_column='TimeEvent', blank=True, null=True, db_comment='Время прихода последнего событ')  # Field name made lowercase.
    opencontrol = models.BooleanField(db_column='OpenControl', blank=True, null=True, db_comment='1 - Контроль открытий по распи')  # Field name made lowercase.
    z8timeout = models.DateTimeField(db_column='Z8Timeout', blank=True, null=True, db_comment='Ожидание звонка с объекта при ')  # Field name made lowercase.
    info = models.ForeignKey('Moreaboutlun7', models.DO_NOTHING, blank=True, null=True, db_comment='MoreAboutLun7.info_id')
    typeschedule = models.IntegerField(db_column='typeSchedule', blank=True, null=True, db_comment='Тип работы группы: 1 - свободн')  # Field name made lowercase.
    armedcall = models.BooleanField(db_column='ArmedCall', blank=True, null=True, db_comment='Ставятся под охрану по звонку:')  # Field name made lowercase.
    disabled = models.BooleanField(blank=True, null=True, db_comment='Группа отключена')
    mustcall = models.BooleanField(db_column='mustCall', blank=True, null=True, db_comment='Обязательный прозвон, при нару')  # Field name made lowercase.
    timeforclose = models.DateTimeField(db_column='TimeForClose', blank=True, null=True, db_comment='Контроль закрытий круглосуточн')  # Field name made lowercase.
    partial = models.CharField(db_column='Partial', max_length=150, blank=True, null=True, db_comment='Не используется')  # Field name made lowercase.
    operatorprompt = models.CharField(db_column='OperatorPrompt', max_length=2000, blank=True, null=True, db_comment='Инструкция по реагированию для')  # Field name made lowercase.
    company = models.ForeignKey(Company, models.DO_NOTHING, db_comment='Company.company_id')
    isprohibited = models.BooleanField(db_column='IsProhibited', blank=True, null=True, db_comment='Признак запрет постановки для ')  # Field name made lowercase.
    autoarmdisarm = models.BooleanField(db_column='AutoArmDisarm')  # Field name made lowercase.
    alarmbuttonphmk = models.BooleanField(db_column='alarmButtonPhMk')  # Field name made lowercase.
    isopenbyaccess = models.BooleanField(db_column='IsOpenByAccess', blank=True, null=True)  # Field name made lowercase.
    intervalpatrolinspection = models.DateTimeField(db_column='IntervalPatrolInspection', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Groups'
        unique_together = (('panel', 'group_field'),)
        db_table_comment = 'Группы объекта'


class Ipcameraservice(models.Model):
    id = models.IntegerField(db_column='Id', primary_key=True)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=100)  # Field name made lowercase.
    inuse = models.BooleanField(db_column='InUse')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'IPCameraService'


class Ipcameras(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=200)  # Field name made lowercase.
    ipcameraserviceid = models.ForeignKey(Ipcameraservice, models.DO_NOTHING, db_column='IPCameraServiceId')  # Field name made lowercase.
    serialnumber = models.CharField(db_column='SerialNumber', max_length=100)  # Field name made lowercase.
    verificationcode = models.CharField(db_column='VerificationCode', max_length=100)  # Field name made lowercase.
    servicelogin = models.CharField(db_column='ServiceLogin', max_length=100)  # Field name made lowercase.
    servicepassword = models.CharField(db_column='ServicePassword', max_length=100)  # Field name made lowercase.
    rtsplink = models.CharField(db_column='RTSPLink', max_length=500)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'IPCameras'


class Imagelist(models.Model):
    imageid = models.AutoField(db_column='ImageId', primary_key=True)  # Field name made lowercase.
    catid = models.IntegerField(db_column='CatId')  # Field name made lowercase.
    imagetype = models.IntegerField(db_column='ImageType')  # Field name made lowercase.
    imagename = models.CharField(db_column='ImageName', max_length=50, blank=True, null=True)  # Field name made lowercase.
    imagedata = models.BinaryField(db_column='ImageData', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ImageList'


class Imagelisttype(models.Model):
    typeid = models.AutoField(db_column='TypeId', primary_key=True)  # Field name made lowercase.
    typetext = models.CharField(db_column='TypeText', max_length=100, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ImageListType'


class Installers(models.Model):
    installer_id = models.AutoField(db_column='Installer_id', primary_key=True, db_comment='ID')  # Field name made lowercase.
    installername = models.CharField(db_column='InstallerName', unique=True, max_length=200, db_comment='ФИО монтажника')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Installers'
        db_table_comment = 'Ответственные монтажники'


class Journalcategories(models.Model):
    category_id = models.AutoField(db_column='Category_id', primary_key=True)  # Field name made lowercase.
    categoryname = models.CharField(db_column='CategoryName', unique=True, max_length=50)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'JournalCategories'


class Journalinvisiblecolumns(models.Model):
    journalinvisiblecolumnid = models.AutoField(db_column='JournalInvisibleColumnID', primary_key=True)  # Field name made lowercase.
    journal = models.ForeignKey('Journals', models.DO_NOTHING, db_column='Journal_id')  # Field name made lowercase.
    fieldname = models.CharField(db_column='FieldName', max_length=300)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'JournalInvisibleColumns'
        unique_together = (('journal', 'fieldname'),)


class Journalparameters(models.Model):
    journal = models.ForeignKey('Journals', models.DO_NOTHING, db_column='Journal_id')  # Field name made lowercase.
    paramname = models.CharField(db_column='ParamName', max_length=50, blank=True, null=True)  # Field name made lowercase.
    paramvalue = models.CharField(db_column='ParamValue', max_length=500, blank=True, null=True)  # Field name made lowercase.
    paramtype = models.IntegerField(db_column='ParamType', blank=True, null=True)  # Field name made lowercase.
    isdefault = models.BooleanField(db_column='isDefault')  # Field name made lowercase.
    ismin = models.BooleanField(db_column='isMin', blank=True, null=True)  # Field name made lowercase.
    ismax = models.BooleanField(db_column='isMax', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'JournalParameters'


class Journalresponsegroupscomments(models.Model):
    journalresponsegroupscommentsid = models.AutoField(db_column='JournalResponseGroupsCommentsID', primary_key=True)  # Field name made lowercase.
    event_id = models.IntegerField(db_column='Event_id')  # Field name made lowercase.
    service_id = models.IntegerField(db_column='Service_id')  # Field name made lowercase.
    comment = models.CharField(db_column='Comment', max_length=4000)  # Field name made lowercase.
    person = models.ForeignKey('Personal', models.DO_NOTHING, db_column='Person_id', blank=True, null=True)  # Field name made lowercase.
    createdate = models.DateTimeField(db_column='CreateDate')  # Field name made lowercase.
    date_key = models.IntegerField(db_column='Date_Key')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'JournalResponseGroupsComments'


class Journals(models.Model):
    journal_id = models.AutoField(db_column='Journal_id', primary_key=True)  # Field name made lowercase.
    journalname = models.CharField(db_column='JournalName', max_length=50)  # Field name made lowercase.
    category = models.ForeignKey(Journalcategories, models.DO_NOTHING, db_column='Category_id', blank=True, null=True)  # Field name made lowercase.
    viewname = models.CharField(db_column='ViewName', max_length=50, blank=True, null=True)  # Field name made lowercase.
    topcount = models.IntegerField(db_column='TopCount', blank=True, null=True)  # Field name made lowercase.
    isdynamic = models.BooleanField(db_column='isDynamic')  # Field name made lowercase.
    viewtext = models.CharField(db_column='ViewText', max_length=7000, blank=True, null=True)  # Field name made lowercase.
    aviable = models.BooleanField(db_column='Aviable', blank=True, null=True)  # Field name made lowercase.
    orderby = models.CharField(db_column='OrderBy', max_length=1000, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Journals'


class LockTimerState(models.Model):
    name = models.CharField(db_column='Name', max_length=50)  # Field name made lowercase.
    computer = models.CharField(db_column='Computer', max_length=70)  # Field name made lowercase.
    result = models.IntegerField(db_column='Result')  # Field name made lowercase.
    is_shutdown = models.IntegerField(db_column='Is_shutdown', blank=True, null=True)  # Field name made lowercase.
    is_message = models.IntegerField(db_column='Is_message', blank=True, null=True)  # Field name made lowercase.
    date = models.DateTimeField(db_column='Date')  # Field name made lowercase.
    date_wd = models.DateTimeField(db_column='Date_wd', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Lock_timer_state'


class Lunproblemstatus(models.Model):
    mphone = models.ForeignKey('Mphone', models.DO_NOTHING, db_column='Mphone_id')  # Field name made lowercase.
    type_device = models.SmallIntegerField(db_column='Type_device')  # Field name made lowercase.
    num = models.IntegerField(db_column='Num', blank=True, null=True)  # Field name made lowercase.
    type_problem = models.SmallIntegerField(db_column='Type_Problem')  # Field name made lowercase.
    problem_date = models.DateTimeField(db_column='Problem_Date')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'LunProblemStatus'


class Lurking(models.Model):
    lurking_id = models.AutoField(db_column='Lurking_id', primary_key=True)  # Field name made lowercase.
    typecode_id = models.IntegerField(db_column='TypeCode_id')  # Field name made lowercase.
    timer = models.DateTimeField(db_column='Timer', blank=True, null=True)  # Field name made lowercase.
    condition = models.ForeignKey('Lurkingconditions', models.DO_NOTHING, db_column='Condition_id', blank=True, null=True)  # Field name made lowercase.
    generatedcode = models.CharField(db_column='GeneratedCode', max_length=6)  # Field name made lowercase.
    generatedcodegroup = models.SmallIntegerField(db_column='GeneratedCodeGroup')  # Field name made lowercase.
    cancel_idtcode = models.IntegerField(db_column='Cancel_idTCode', blank=True, null=True)  # Field name made lowercase.
    needdropold = models.BooleanField(db_column='NeedDropOld', blank=True, null=True)  # Field name made lowercase.
    iscentral = models.BooleanField(db_column='IsCentral')  # Field name made lowercase.
    repetitivetimer = models.BooleanField(db_column='RepetitiveTimer', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Lurking'


class Lurkingconditions(models.Model):
    condition_id = models.AutoField(db_column='Condition_id', primary_key=True)  # Field name made lowercase.
    conditiontext = models.CharField(db_column='ConditionText', max_length=1000)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'LurkingConditions'


class Mphone(models.Model):
    mphone_id = models.AutoField(db_column='Mphone_id', primary_key=True, db_comment='ID')  # Field name made lowercase.
    panel = models.ForeignKey('Panel', models.DO_NOTHING, db_column='Panel_id', blank=True, null=True, db_comment='Panel.Panel_id')  # Field name made lowercase.
    rstartdate = models.DateTimeField(db_column='RStartDate', blank=True, null=True, db_comment='Дата подключения')  # Field name made lowercase.
    radioversion = models.CharField(db_column='RadioVersion', max_length=50, blank=True, null=True, db_comment='Версия прибора')  # Field name made lowercase.
    radiotype = models.ForeignKey('Mphoneradiotype', models.DO_NOTHING, db_column='RadioType', blank=True, null=True, db_comment='MphoneRadioType.RadioType_id')  # Field name made lowercase.
    codegroup = models.SmallIntegerField(db_column='CodeGroup', db_comment='Указанный вручную набор кодов')  # Field name made lowercase.
    mainpower = models.BooleanField(db_column='MainPower', blank=True, null=True, db_comment='Основное питание: 1 - есть; 0 ')  # Field name made lowercase.
    backuppower = models.BooleanField(db_column='BackupPower', blank=True, null=True, db_comment='Резервное питание: 1 - есть; 0')  # Field name made lowercase.
    mptime = models.DateTimeField(db_column='MPTime', blank=True, null=True, db_comment='Время последнего изменения сос')  # Field name made lowercase.
    bptime = models.DateTimeField(db_column='BPTime', blank=True, null=True, db_comment='Время последнего изменения сос')  # Field name made lowercase.
    typetransmitter = models.ForeignKey('Mphonetypetransmitter', models.DO_NOTHING, db_column='TypeTransmitter', blank=True, null=True, db_comment='MphoneTypeTransmitter.TypeTran')  # Field name made lowercase.
    isjablotron = models.BooleanField(db_column='IsJablotron', blank=True, null=True, db_comment='К прибору подключен ППК Jablot')  # Field name made lowercase.
    dot3 = models.BooleanField(db_column='DOT3', blank=True, null=True, db_comment='Использовать короткий протокол')  # Field name made lowercase.
    lasttest = models.DateTimeField(db_column='LastTest', blank=True, null=True, db_comment='Дата и время последнего теста')  # Field name made lowercase.
    lastgprscount = models.IntegerField(db_column='LastGPRSCount', blank=True, null=True, db_comment='Текущий счетчик события')  # Field name made lowercase.
    signallevel = models.SmallIntegerField(db_column='SignalLevel', blank=True, null=True, db_comment='Уровень сигнала')  # Field name made lowercase.
    signaldate = models.DateTimeField(db_column='SignalDate', blank=True, null=True, db_comment='Дата уровня сигнала')  # Field name made lowercase.
    isreference = models.IntegerField(db_column='IsReference', blank=True, null=True, db_comment='Сделать прибор "эталонным": 1 ')  # Field name made lowercase.
    workmode = models.SmallIntegerField(db_column='WorkMode', blank=True, null=True, db_comment='Режим работы прибора: 0 - толь')  # Field name made lowercase.
    currentchannel = models.ForeignKey(Channeltypes, models.DO_NOTHING, db_column='CurrentChannel_id', blank=True, null=True, db_comment='Channels.ChannelType_id')  # Field name made lowercase.
    currenttemperature = models.CharField(db_column='CurrentTemperature', max_length=10, blank=True, null=True, db_comment='Температура модуля')  # Field name made lowercase.
    statusz2 = models.BooleanField(db_column='StatusZ2', blank=True, null=True, db_comment='Было ли событие Z2: 1 - да; 0 ')  # Field name made lowercase.
    islindconnect = models.BooleanField(db_column='isLindConnect', blank=True, null=True, db_comment='Состояние Линда: 1 - подключен')  # Field name made lowercase.
    islindconnecttime = models.DateTimeField(db_column='isLindConnectTime', blank=True, null=True, db_comment='Время последнего состояния')  # Field name made lowercase.
    issafeppkp = models.BooleanField(db_column='isSafePPKP', blank=True, null=True, db_comment='Целостность ППК: 1 - да; 0 - н')  # Field name made lowercase.
    issafeppkptime = models.DateTimeField(db_column='isSafePPKPTime', blank=True, null=True, db_comment='Дата и время последнего измене')  # Field name made lowercase.
    issirenaconnect = models.BooleanField(db_column='isSirenaConnect', blank=True, null=True, db_comment='Сирена подключена: 1 - да; 0 -')  # Field name made lowercase.
    issirenaconnecttime = models.DateTimeField(db_column='isSirenaConnectTime', blank=True, null=True, db_comment='Дата и время последнего измене')  # Field name made lowercase.
    ispultconnect = models.BooleanField(db_column='isPultConnect', blank=True, null=True, db_comment='Связь с пультом: 1 - есть; 0 -')  # Field name made lowercase.
    ispultconnecttime = models.DateTimeField(db_column='isPultConnectTime', blank=True, null=True, db_comment='Дата и время последнего измене')  # Field name made lowercase.
    funcmainpower = models.BooleanField(db_column='FuncMainPower', blank=True, null=True, db_comment='Включение функции основного пи')  # Field name made lowercase.
    funcmainpowertime = models.DateTimeField(db_column='FuncMainPowerTime', blank=True, null=True, db_comment='Дата и время изменения состоян')  # Field name made lowercase.
    funcbackuppower = models.BooleanField(db_column='FuncBackupPower', blank=True, null=True, db_comment='Включение функции резервного п')  # Field name made lowercase.
    funcbackuppowertime = models.DateTimeField(db_column='FuncBackupPowerTime', blank=True, null=True, db_comment='Дата и время изменения состоян')  # Field name made lowercase.
    funcrele2 = models.BooleanField(db_column='FuncRele2', blank=True, null=True, db_comment='Включение функции Реле2: 1 - д')  # Field name made lowercase.
    funcrele2time = models.DateTimeField(db_column='FuncRele2Time', blank=True, null=True, db_comment='Дата и время последенего состо')  # Field name made lowercase.
    funcrele1 = models.BooleanField(db_column='FuncRele1', blank=True, null=True, db_comment='Включение функции Реле1: 1 - д')  # Field name made lowercase.
    funcrele1time = models.DateTimeField(db_column='FuncRele1Time', blank=True, null=True, db_comment='Дата и время последенего состо')  # Field name made lowercase.
    funcsensorspower = models.BooleanField(db_column='FuncSensorsPower', blank=True, null=True, db_comment='Включение функции датчика пита')  # Field name made lowercase.
    funcsensorspowertime = models.DateTimeField(db_column='FuncSensorsPowerTime', blank=True, null=True, db_comment='Дата и время последнего измене')  # Field name made lowercase.
    funcsirenastate = models.BooleanField(db_column='FuncSirenaState', blank=True, null=True, db_comment='Включение функции сирена: 1 - ')  # Field name made lowercase.
    funcsirenastatetime = models.DateTimeField(db_column='FuncSirenaStateTime', blank=True, null=True, db_comment='Дата и время последнего измене')  # Field name made lowercase.
    funcpultconnect = models.BooleanField(db_column='FuncPultConnect', blank=True, null=True, db_comment='Включение функции соединения с')  # Field name made lowercase.
    funcpultconnecttime = models.DateTimeField(db_column='FuncPultConnectTime', blank=True, null=True, db_comment='Дата и время последнего измене')  # Field name made lowercase.
    levelacs = models.IntegerField(db_column='levelAcs', db_comment='Вход на уровень доступа')  # Field name made lowercase.
    levelacstime = models.DateTimeField(db_column='levelAcsTime', blank=True, null=True, db_comment='Время входа на уровень доступа')  # Field name made lowercase.
    issirenasounding = models.BooleanField(db_column='isSirenaSounding', blank=True, null=True, db_comment='Звук сирены включен: 1 - да; 0')  # Field name made lowercase.
    issirenasoundingtime = models.DateTimeField(db_column='isSirenaSoundingTime', blank=True, null=True, db_comment='Дата и время последнего измене')  # Field name made lowercase.
    issensorspower = models.BooleanField(db_column='isSensorsPower', blank=True, null=True, db_comment='Датчик питания включен: 1 - да')  # Field name made lowercase.
    issensorspowertime = models.DateTimeField(db_column='isSensorsPowerTime', blank=True, null=True, db_comment='Дата и время последнего измене')  # Field name made lowercase.
    rele1state = models.BooleanField(db_column='Rele1State', blank=True, null=True, db_comment='Состояние Реле1: 1 - включено;')  # Field name made lowercase.
    rele1statetime = models.DateTimeField(db_column='Rele1StateTime', blank=True, null=True, db_comment='Дата и время последнего измене')  # Field name made lowercase.
    rele2state = models.BooleanField(db_column='Rele2State', blank=True, null=True, db_comment='Состояние Реле2: 1 - включено;')  # Field name made lowercase.
    rele2statetime = models.DateTimeField(db_column='Rele2StateTime', blank=True, null=True, db_comment='Дата и время последнего измене')  # Field name made lowercase.
    lastresetkeyboardtime = models.DateTimeField(db_column='LastResetKeyBoardTime', blank=True, null=True, db_comment='Дата и время последнего сброса')  # Field name made lowercase.
    lastresetpulttime = models.DateTimeField(db_column='LastResetPultTime', blank=True, null=True, db_comment='Дата и время последнего сброса')  # Field name made lowercase.
    islinetan = models.BooleanField(db_column='isLineTAN', blank=True, null=True, db_comment='Признак линии TAN: 1 - да; 0 -')  # Field name made lowercase.
    islinetantime = models.DateTimeField(db_column='isLineTANTime', blank=True, null=True, db_comment='Дата и время последнего измене')  # Field name made lowercase.
    currentsim = models.ForeignKey('Sims', models.DO_NOTHING, db_column='CurrentSIM', blank=True, null=True, db_comment='Текущая Sim карта, на которой ')  # Field name made lowercase.
    isreportwaiting = models.SmallIntegerField(db_column='IsReportWaiting', blank=True, null=True, db_comment='Ожидание отчета')  # Field name made lowercase.
    metercount = models.CharField(db_column='MeterCount', max_length=50, blank=True, null=True, db_comment='Показание электросчетчика')  # Field name made lowercase.
    timemetercount = models.DateTimeField(db_column='TimeMeterCount', blank=True, null=True, db_comment='Дата и время последнего показа')  # Field name made lowercase.
    isprohibited = models.BooleanField(db_column='IsProhibited', blank=True, null=True, db_comment='Признак запрета постановки под')  # Field name made lowercase.
    filinversion = models.CharField(db_column='FilinVersion', max_length=50, blank=True, null=True, db_comment='Версия ТК')  # Field name made lowercase.
    compatibilitydata = models.SmallIntegerField(db_column='CompatibilityData', blank=True, null=True, db_comment='Системное поле')  # Field name made lowercase.
    deviceversion = models.SmallIntegerField(db_column='DeviceVersion', blank=True, null=True, db_comment='Реальная версия прибора')  # Field name made lowercase.
    compatibilityiswaiting = models.SmallIntegerField(db_column='CompatibilityIsWaiting', blank=True, null=True, db_comment='Системное поле')  # Field name made lowercase.
    protocoltype = models.SmallIntegerField(db_column='ProtocolType', db_comment='Тип протокола: 0 - для всех лу')  # Field name made lowercase.
    macaddress = models.CharField(db_column='MacAddress', max_length=10, blank=True, null=True, db_comment='MAC-адрес')  # Field name made lowercase.
    lastlatitude = models.CharField(db_column='LastLatitude', max_length=20, blank=True, null=True, db_comment='Последенее значение GPS коорди')  # Field name made lowercase.
    lastlongtitude = models.CharField(db_column='LastLongtitude', max_length=20, blank=True, null=True, db_comment='Последенее значение GPS коорди')  # Field name made lowercase.
    gpsarrivetime = models.DateTimeField(db_column='GPSArriveTime', blank=True, null=True, db_comment='Время последнего прихода GPS к')  # Field name made lowercase.
    isgpsvalid = models.BooleanField(db_column='isGPSValid', blank=True, null=True, db_comment='Валидность координат: 1 - да; ')  # Field name made lowercase.
    isallowbatterycharging = models.BooleanField(db_column='isAllowBatteryCharging', blank=True, null=True, db_comment='Разрешена ли зарядка АКБ Алета')  # Field name made lowercase.
    powergps = models.BooleanField(db_column='PowerGPS', blank=True, null=True, db_comment='Включен ли GPS приемник: 1 - д')  # Field name made lowercase.
    aletbatterychargelevel = models.CharField(db_column='AletBatteryChargeLevel', max_length=3, blank=True, null=True, db_comment='Уровень заряда батареи Алета в')  # Field name made lowercase.
    aletbatteryvoltage = models.CharField(db_column='AletBatteryVoltage', max_length=5, blank=True, null=True, db_comment='Уровень заряда батареи Алета в')  # Field name made lowercase.
    timegetaletbatterystate = models.DateTimeField(db_column='TimeGetAletBatteryState', blank=True, null=True, db_comment='Время последнего опроса уровня')  # Field name made lowercase.
    insecurelat = models.CharField(db_column='InSecureLat', max_length=20, blank=True, null=True, db_comment='Координаты широты при постанов')  # Field name made lowercase.
    insecurelon = models.CharField(db_column='InSecureLon', max_length=20, blank=True, null=True, db_comment='Координаты долготы при постано')  # Field name made lowercase.
    insecurestatus = models.CharField(db_column='InSecureStatus', max_length=1, blank=True, null=True, db_comment='Тип полученных координат:\r\nL -')  # Field name made lowercase.
    insecuretime = models.DateTimeField(db_column='InSecureTime', blank=True, null=True, db_comment='Дата и время последнего получе')  # Field name made lowercase.
    lastcourseoverground = models.CharField(db_column='LastCourseOverGround', max_length=10, blank=True, null=True, db_comment='Последнее направление движения')  # Field name made lowercase.
    lancomversion = models.CharField(db_column='LanComVersion', max_length=50, blank=True, null=True, db_comment='Версия LanCom')  # Field name made lowercase.
    testtimeoutreserved = models.DateTimeField(db_column='TestTimeoutReserved', blank=True, null=True, db_comment='Период тестирования резервной ')  # Field name made lowercase.
    aletakbdate = models.DateTimeField(db_column='AletAkbDate', blank=True, null=True)  # Field name made lowercase.
    aletmod = models.CharField(db_column='AletMod', max_length=10, blank=True, null=True)  # Field name made lowercase.
    aletblackbox = models.BooleanField(db_column='AletBlackBox', blank=True, null=True)  # Field name made lowercase.
    isgpstracker = models.IntegerField(db_column='IsGPSTracker')  # Field name made lowercase.
    cpid = models.CharField(db_column='CpId', max_length=16, blank=True, null=True)  # Field name made lowercase.
    currentsim2channel = models.ForeignKey(Channeltypes, models.DO_NOTHING, db_column='CurrentSim2Channel_id', related_name='mphone_currentsim2channel_set', blank=True, null=True)  # Field name made lowercase.
    usealternativetesting = models.BooleanField(db_column='UseAlternativeTesting')  # Field name made lowercase.
    nottested = models.BooleanField(db_column='NotTested')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'MPhone'
        db_table_comment = 'Оборудование, установленное на'


class Mphoneradioseries(models.Model):
    series_id = models.SmallIntegerField(db_column='Series_id', primary_key=True)  # Field name made lowercase.
    seriesname = models.CharField(db_column='SeriesName', max_length=20, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'MPhoneRadioSeries'


class Manualaddedalarmobject(models.Model):
    objectid = models.AutoField(db_column='ObjectID', primary_key=True)  # Field name made lowercase.
    panel_id = models.CharField(db_column='Panel_id', max_length=20, blank=True, null=True)  # Field name made lowercase.
    lat = models.CharField(max_length=20, blank=True, null=True)
    lon = models.CharField(max_length=20, blank=True, null=True)
    createdate = models.DateTimeField(db_column='CreateDate', blank=True, null=True)  # Field name made lowercase.
    compcreate = models.CharField(db_column='CompCreate', max_length=20, blank=True, null=True)  # Field name made lowercase.
    deletedate = models.DateTimeField(db_column='DeleteDate', blank=True, null=True)  # Field name made lowercase.
    compdelete = models.CharField(db_column='CompDelete', max_length=20, blank=True, null=True)  # Field name made lowercase.
    isended = models.BooleanField(db_column='isEnded', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ManualAddedAlarmObject'


class Marktypes(models.Model):
    marktype_id = models.SmallAutoField(db_column='MarkType_id', primary_key=True)  # Field name made lowercase.
    marktypemessage = models.CharField(db_column='MarkTypeMessage', unique=True, max_length=100)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'MarkTypes'


class Marks(models.Model):
    panel = models.OneToOneField(Groups, models.DO_NOTHING, db_column='Panel_id', primary_key=True, db_comment='Groups.Panel_id')  # Field name made lowercase. The composite primary key (Panel_id, group_, Mark_Type_id) found, that is not supported. The first column is selected.
    group_field = models.ForeignKey(Groups, models.DO_NOTHING, db_column='group_', related_name='marks_group_field_set', db_comment='Groups.Group_')  # Field renamed because it ended with '_'.
    mark_message = models.CharField(db_column='Mark_Message', max_length=200, db_comment='?')  # Field name made lowercase.
    mark_date = models.DateTimeField(db_column='Mark_Date', db_comment='?')  # Field name made lowercase.
    mark_elapseddate = models.DateTimeField(db_column='Mark_ElapsedDate', blank=True, null=True, db_comment='?')  # Field name made lowercase.
    mark_type_id = models.SmallIntegerField(db_column='Mark_Type_id', db_comment='?')  # Field name made lowercase.
    person = models.ForeignKey('Personal', models.DO_NOTHING, db_column='Person_id', blank=True, null=True, db_comment='Personal.Person_Id')  # Field name made lowercase.
    personnamedeleted = models.CharField(db_column='PersonNameDeleted', max_length=200, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Marks'
        unique_together = (('panel', 'group_field', 'mark_type_id'),)
        db_table_comment = '?'


class Masters(models.Model):
    master_id = models.AutoField(db_column='Master_id', primary_key=True, db_comment='ID')  # Field name made lowercase.
    mastername = models.CharField(db_column='MasterName', unique=True, max_length=200, db_comment='ФИО мастера')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Masters'
        db_table_comment = 'Ответственные мастера'


class Mobileevents(models.Model):
    archiveid = models.IntegerField(db_column='archiveId', primary_key=True)  # Field name made lowercase. The composite primary key (archiveId, userId) found, that is not supported. The first column is selected.
    userid = models.ForeignKey('Mobileuser', models.DO_NOTHING, db_column='userId')  # Field name made lowercase.
    panel = models.CharField(max_length=16)
    group = models.IntegerField()
    zone = models.IntegerField(blank=True, null=True)
    typecode = models.IntegerField(db_column='typeCode', blank=True, null=True)  # Field name made lowercase.
    eventmessage = models.CharField(db_column='eventMessage', max_length=1000)  # Field name made lowercase.
    timeevent = models.DateTimeField(db_column='timeEvent')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'MobileEvents'
        unique_together = (('archiveid', 'userid'),)


class Mobileremotecontrol(models.Model):
    remcontrolid = models.AutoField(db_column='remControlId', primary_key=True)  # Field name made lowercase.
    userid = models.ForeignKey('Mobileuser', models.DO_NOTHING, db_column='userId', blank=True, null=True)  # Field name made lowercase.
    callid = models.CharField(db_column='callId', max_length=50, blank=True, null=True)  # Field name made lowercase.
    commandid = models.IntegerField(db_column='commandId', blank=True, null=True)  # Field name made lowercase.
    panelid = models.CharField(db_column='PanelId', max_length=20, blank=True, null=True)  # Field name made lowercase.
    group = models.IntegerField(db_column='Group', blank=True, null=True)  # Field name made lowercase.
    zone = models.IntegerField(db_column='Zone', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'MobileRemoteControl'


class Mobilesettings(models.Model):
    compname = models.CharField(db_column='CompName', max_length=16, blank=True, null=True)  # Field name made lowercase.
    serverip = models.CharField(db_column='serverIp', max_length=16, blank=True, null=True)  # Field name made lowercase.
    port = models.IntegerField(blank=True, null=True)
    allowunconditionalarmed = models.BooleanField(db_column='allowUnconditionalArmed')  # Field name made lowercase.
    enabled = models.BooleanField(db_column='Enabled')  # Field name made lowercase.
    allowsendtestchanged = models.BooleanField(db_column='allowSendTestChanged')  # Field name made lowercase.
    imgserverip = models.CharField(db_column='imgServerIp', max_length=20, blank=True, null=True)  # Field name made lowercase.
    imgserverport = models.IntegerField(db_column='imgServerPort', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'MobileSettings'


class Mobileuser(models.Model):
    userid = models.AutoField(db_column='userId', primary_key=True)  # Field name made lowercase.
    login = models.CharField(unique=True, max_length=50, blank=True, null=True)
    password = models.CharField(max_length=100)
    imei = models.CharField(max_length=50, blank=True, null=True)
    banstate = models.BooleanField(db_column='banState')  # Field name made lowercase.
    evtcounter = models.IntegerField(db_column='evtCounter')  # Field name made lowercase.
    onlinestate = models.ForeignKey('Mobileuseronlinestate', models.DO_NOTHING, db_column='onlineState')  # Field name made lowercase.
    currentpackage = models.CharField(db_column='currentPackage', max_length=5000, blank=True, null=True)  # Field name made lowercase.
    roleid = models.ForeignKey('Mobileuserrole', models.DO_NOTHING, db_column='roleId')  # Field name made lowercase.
    forcepassword = models.CharField(db_column='forcePassword', max_length=100, blank=True, null=True)  # Field name made lowercase.
    eventforallgr = models.IntegerField(db_column='eventForAllGr')  # Field name made lowercase.
    language = models.CharField(max_length=2, blank=True, null=True)
    responsibleslist = models.ForeignKey('Responsibleslist', models.DO_NOTHING, db_column='ResponsiblesList_id', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'MobileUser'


class Mobileuserbalance(models.Model):
    contractid = models.CharField(db_column='contractId', primary_key=True, max_length=100)  # Field name made lowercase.
    balance = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'MobileUserBalance'


class Mobileuserchanged(models.Model):
    changedid = models.AutoField(db_column='changedId', primary_key=True)  # Field name made lowercase.
    userid = models.IntegerField(db_column='userId')  # Field name made lowercase.
    login = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'MobileUserChanged'


class Mobileuseronlinestate(models.Model):
    stateid = models.IntegerField(db_column='stateId', primary_key=True)  # Field name made lowercase.
    description = models.CharField(db_column='Description', max_length=30, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'MobileUserOnlineState'


class Mobileuserrole(models.Model):
    roleid = models.IntegerField(db_column='roleId', primary_key=True)  # Field name made lowercase.
    rolename = models.CharField(db_column='roleName', max_length=50, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'MobileUserRole'


class Mobileusersubscribe(models.Model):
    usergrid = models.OneToOneField('MobileuserGroups', models.DO_NOTHING, db_column='userGrId', primary_key=True)  # Field name made lowercase. The composite primary key (userGrId, typeCodeId) found, that is not supported. The first column is selected.
    typecodeid = models.ForeignKey('Typecode', models.DO_NOTHING, db_column='typeCodeId')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'MobileUserSubscribe'
        unique_together = (('usergrid', 'typecodeid'),)


class MobileuserGroups(models.Model):
    usergrid = models.AutoField(db_column='userGrId', unique=True)  # Field name made lowercase.
    userid = models.OneToOneField(Mobileuser, models.DO_NOTHING, db_column='userId', primary_key=True)  # Field name made lowercase. The composite primary key (userId, panelId, group) found, that is not supported. The first column is selected.
    panelid = models.ForeignKey(Groups, models.DO_NOTHING, db_column='panelId')  # Field name made lowercase.
    group = models.ForeignKey(Groups, models.DO_NOTHING, db_column='group', related_name='mobileusergroups_group_set')

    class Meta:
        managed = False
        db_table = 'MobileUser_Groups'
        unique_together = (('userid', 'panelid', 'group'),)


class Moreaboutlun7(models.Model):
    info_id = models.AutoField(primary_key=True, db_comment='ID')
    mainpower = models.BooleanField(db_column='MainPower', blank=True, null=True, db_comment='Основное питание: 1 - есть; 0 ')  # Field name made lowercase.
    backuppower = models.BooleanField(db_column='BackupPower', blank=True, null=True, db_comment='Резервное питание: 1 - есть; 0')  # Field name made lowercase.
    mptime = models.DateTimeField(db_column='MPTime', blank=True, null=True, db_comment='Время последнего изменения сос')  # Field name made lowercase.
    bptime = models.DateTimeField(db_column='BPTime', blank=True, null=True, db_comment='Время последнего изменения сос')  # Field name made lowercase.
    version = models.CharField(max_length=20, blank=True, null=True, db_comment='Версия')
    codegroup_unused = models.SmallIntegerField(db_column='CodeGroup_unused', blank=True, null=True, db_comment='Набор кодов')  # Field name made lowercase.
    isconnected = models.BooleanField(db_column='isConnected', blank=True, null=True, db_comment='Есть соединение: 1 - да; 0 - н')  # Field name made lowercase.
    datechangeconnect = models.DateTimeField(db_column='DateChangeConnect', blank=True, null=True, db_comment='Дата последнего изменения сост')  # Field name made lowercase.
    extype = models.ForeignKey(Extensiontypes, models.DO_NOTHING, db_column='ExType_id', blank=True, null=True, db_comment='Подключенное расширение')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'MoreAboutLun7'
        db_table_comment = 'Дополнительная информация по Л'


class Mphoneradiotype(models.Model):
    radiotype_id = models.AutoField(db_column='RadioType_id', primary_key=True, db_comment='ID')  # Field name made lowercase.
    message = models.CharField(db_column='Message', max_length=50, blank=True, null=True, db_comment='Тип прибора')  # Field name made lowercase.
    series_id = models.SmallIntegerField(db_column='Series_id', blank=True, null=True, db_comment='Серия приборов: 1 - 5-ая серия')  # Field name made lowercase.
    isuse = models.BooleanField(db_column='IsUse', blank=True, null=True, db_comment='Доступен: 1 - да; 0 - нет')  # Field name made lowercase.
    deviceid = models.SmallIntegerField(db_column='DeviceId', db_comment='Типы луней (TLunList)')  # Field name made lowercase.
    versionupdateallowed = models.SmallIntegerField(db_column='VersionUpdateAllowed', blank=True, null=True, db_comment='Минимальная версия, с которой ')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'MphoneRadioType'
        db_table_comment = 'Типы приборов'


class Mphonetypetransmitter(models.Model):
    typetransmitter_id = models.IntegerField(db_column='TypeTransmitter_id', primary_key=True, db_comment='ID')  # Field name made lowercase.
    message = models.CharField(db_column='Message', max_length=50, blank=True, null=True, db_comment='Тип передатчика')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'MphoneTypeTransmitter'
        db_table_comment = 'Типы передатчиков'


class Objschedule(models.Model):
    recordid = models.AutoField(db_column='RecordID', primary_key=True, db_comment='ID')  # Field name made lowercase.
    panelid = models.ForeignKey(Groups, models.DO_NOTHING, db_column='PanelID', db_comment='Groups.Panel_id')  # Field name made lowercase.
    group_field = models.ForeignKey(Groups, models.DO_NOTHING, db_column='Group_', related_name='objschedule_group_field_set', db_comment='Groups.Group_')  # Field name made lowercase. Field renamed because it ended with '_'.
    daynumber = models.IntegerField(db_column='DayNumber', blank=True, null=True, db_comment='День недели (1 - пн.; 2 - вт.;')  # Field name made lowercase.
    intervalnumber = models.IntegerField(db_column='IntervalNumber', blank=True, null=True, db_comment='Порядковый номер расписания в ')  # Field name made lowercase.
    startdt = models.DateTimeField(db_column='StartDT', blank=True, null=True, db_comment='Начальное время, когда объект ')  # Field name made lowercase.
    stopdt = models.DateTimeField(db_column='StopDT', blank=True, null=True, db_comment='Конечное время, когда объект п')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ObjSchedule'
        db_table_comment = 'Расписания работы группы'


class Objectaddinfo(models.Model):
    objectaddinfoid = models.AutoField(db_column='ObjectAddInfoID')  # Field name made lowercase.
    panelid = models.OneToOneField(Groups, models.DO_NOTHING, db_column='PanelID', primary_key=True)  # Field name made lowercase. The composite primary key (PanelID, GroupID, AttributeID) found, that is not supported. The first column is selected.
    groupid = models.ForeignKey(Groups, models.DO_NOTHING, db_column='GroupID', related_name='objectaddinfo_groupid_set')  # Field name made lowercase.
    attributeid = models.ForeignKey(Dictentattrval, models.DO_NOTHING, db_column='AttributeID')  # Field name made lowercase.
    valueid = models.ForeignKey(Dictentattrval, models.DO_NOTHING, db_column='ValueID', related_name='objectaddinfo_valueid_set', blank=True, null=True)  # Field name made lowercase.
    value = models.CharField(db_column='Value', max_length=4000, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ObjectAddInfo'
        unique_together = (('panelid', 'groupid', 'attributeid'),)


class Onlineaccessusers(models.Model):
    user_id = models.AutoField(db_column='User_Id', primary_key=True)  # Field name made lowercase.
    user_login = models.CharField(db_column='User_Login', unique=True, max_length=50)  # Field name made lowercase.
    user_password = models.CharField(db_column='User_Password', max_length=50, blank=True, null=True)  # Field name made lowercase.
    saltforpwd = models.CharField(db_column='SaltForPwd', max_length=50, blank=True, null=True)  # Field name made lowercase.
    company_name = models.CharField(db_column='Company_Name', max_length=250, blank=True, null=True)  # Field name made lowercase.
    contract_number = models.CharField(db_column='Contract_Number', max_length=50, blank=True, null=True)  # Field name made lowercase.
    responsibleslist_id = models.IntegerField(db_column='ResponsiblesList_id', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'OnlineAccessUsers'


class OnlineaccessusersPanel(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    user = models.ForeignKey(Onlineaccessusers, models.DO_NOTHING, db_column='User_id')  # Field name made lowercase.
    panel = models.ForeignKey('Panel', models.DO_NOTHING, db_column='Panel_id')  # Field name made lowercase.
    group_field = models.IntegerField(db_column='Group_', blank=True, null=True)  # Field name made lowercase. Field renamed because it ended with '_'.

    class Meta:
        managed = False
        db_table = 'OnlineAccessUsers_Panel'


class Onlinemapsetting(models.Model):
    host = models.CharField(db_column='Host', max_length=16, blank=True, null=True)  # Field name made lowercase.
    settings = models.CharField(db_column='Settings', max_length=8000, blank=True, null=True)  # Field name made lowercase.
    checkgps = models.CharField(db_column='CheckGPS', max_length=8000, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'OnlineMapSetting'


class Openinternetdevices(models.Model):
    number = models.IntegerField(db_column='Number', primary_key=True)  # Field name made lowercase.
    internetdevicename = models.CharField(db_column='InternetDeviceName', max_length=50)  # Field name made lowercase.
    ip = models.CharField(db_column='IP', max_length=15)  # Field name made lowercase.
    isemizontype = models.BooleanField(db_column='isEmizonType')  # Field name made lowercase.
    customernum = models.CharField(db_column='CustomerNum', max_length=50, blank=True, null=True)  # Field name made lowercase.
    customerleg = models.CharField(db_column='CustomerLeg', max_length=50, blank=True, null=True)  # Field name made lowercase.
    customerkey = models.CharField(db_column='CustomerKey', max_length=50, blank=True, null=True)  # Field name made lowercase.
    customerport = models.CharField(db_column='CustomerPort', max_length=50, blank=True, null=True)  # Field name made lowercase.
    port = models.IntegerField(db_column='Port', blank=True, null=True)  # Field name made lowercase.
    ftpip = models.CharField(db_column='FtpIp', max_length=15, blank=True, null=True)  # Field name made lowercase.
    ftpport = models.CharField(db_column='FtpPort', max_length=5, blank=True, null=True)  # Field name made lowercase.
    computername = models.CharField(db_column='ComputerName', max_length=70, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'OpenInternetDevices'


class Operation(models.Model):
    operationname = models.CharField(db_column='OperationName', max_length=150)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Operation'


class Operator(models.Model):
    name = models.CharField(db_column='Name', primary_key=True, max_length=10)  # Field name made lowercase.
    password = models.CharField(db_column='Password', max_length=10, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Operator'


class Operators(models.Model):
    operator_id = models.AutoField(db_column='Operator_id', primary_key=True, db_comment='ID')  # Field name made lowercase.
    operatorname = models.CharField(db_column='OperatorName', unique=True, max_length=200, blank=True, null=True, db_comment='Оператор услуг мобильной связи')  # Field name made lowercase.
    voiceorlansbus_id = models.IntegerField(db_column='VoiceOrlansBus_id', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Operators'
        db_table_comment = 'Операторы услуг мобильной связ'


class Orlanbuses(models.Model):
    bus_number = models.IntegerField(db_column='Bus_number', primary_key=True, db_comment='ID')  # Field name made lowercase.
    bus_name = models.CharField(db_column='Bus_name', max_length=15, db_comment='Название источника событий')  # Field name made lowercase.
    com = models.CharField(db_column='COM', max_length=6, db_comment='Последовательный порт')  # Field name made lowercase.
    orlans = models.SmallIntegerField(db_column='Orlans', db_comment='Количество орланов')  # Field name made lowercase.
    orlanarmed = models.SmallIntegerField(db_column='OrlanArmed', blank=True, null=True, db_comment='№ Орлан-М для удаленной постан')  # Field name made lowercase.
    orlanaux = models.SmallIntegerField(db_column='OrlanAUX', blank=True, null=True, db_comment='№ Орлан-М для выключения AUX /')  # Field name made lowercase.
    orlanreport = models.SmallIntegerField(db_column='OrlanReport', blank=True, null=True, db_comment='№ Орлан-М для отчета и снятия ')  # Field name made lowercase.
    orlanban = models.SmallIntegerField(db_column='OrlanBan', blank=True, null=True, db_comment='№ Орлан-М для запрета постанов')  # Field name made lowercase.
    orlanchangesim = models.SmallIntegerField(db_column='OrlanChangeSim', blank=True, null=True, db_comment='№ Орлан-М для принудительной с')  # Field name made lowercase.
    reserveoperator = models.BooleanField(db_column='ReserveOperator', db_comment='Указать параметры для резервно')  # Field name made lowercase.
    orlanarmedsim2 = models.SmallIntegerField(db_column='OrlanArmedSim2', blank=True, null=True, db_comment='№ Орлан-М для удаленной постан')  # Field name made lowercase.
    orlanauxsim2 = models.SmallIntegerField(db_column='OrlanAUXSim2', blank=True, null=True, db_comment='№ Орлан-М для выключения AUX /')  # Field name made lowercase.
    orlanreportsim2 = models.SmallIntegerField(db_column='OrlanReportSim2', blank=True, null=True, db_comment='№ Орлан-М для отчета и снятия ')  # Field name made lowercase.
    orlanbansim2 = models.SmallIntegerField(db_column='OrlanBanSim2', blank=True, null=True, db_comment='№ Орлан-М для запрета постанов')  # Field name made lowercase.
    orlanchangesimsim2 = models.SmallIntegerField(db_column='OrlanChangeSimSim2', blank=True, null=True, db_comment='№ Орлан-М для принудительной с')  # Field name made lowercase.
    installcomputer = models.CharField(db_column='InstallComputer', max_length=70, blank=True, null=True, db_comment='Источник событий включен (указ')  # Field name made lowercase.
    parentbus_id = models.IntegerField(db_column='ParentBus_id', blank=True, null=True, db_comment='Является расширением шины (Orl')  # Field name made lowercase.
    orlanout = models.SmallIntegerField(db_column='OrlanOut', blank=True, null=True, db_comment='№ Орлан-М для выключения выход')  # Field name made lowercase.
    orlanout2 = models.SmallIntegerField(db_column='OrlanOut2', blank=True, null=True, db_comment='№ Орлан-М для выключения выход')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'OrlanBuses'
        db_table_comment = 'Источники событий по голосовом'


class Orlanchecking(models.Model):
    busnumber_from = models.OneToOneField('Orlanlist', models.DO_NOTHING, db_column='BusNumber_From', primary_key=True)  # Field name made lowercase. The composite primary key (BusNumber_From, OrlanNumber_From, BusNumber_To, OrlanNumber_To) found, that is not supported. The first column is selected.
    orlannumber_from = models.ForeignKey('Orlanlist', models.DO_NOTHING, db_column='OrlanNumber_From', to_field='OrlanNumber', related_name='orlanchecking_orlannumber_from_set')  # Field name made lowercase.
    busnumber_to = models.ForeignKey('Orlanlist', models.DO_NOTHING, db_column='BusNumber_To', to_field='OrlanNumber', related_name='orlanchecking_busnumber_to_set')  # Field name made lowercase.
    orlannumber_to = models.ForeignKey('Orlanlist', models.DO_NOTHING, db_column='OrlanNumber_To', to_field='OrlanNumber', related_name='orlanchecking_orlannumber_to_set')  # Field name made lowercase.
    checkcsd = models.BooleanField(db_column='CheckCSD')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'OrlanChecking'
        unique_together = (('busnumber_from', 'orlannumber_from', 'busnumber_to', 'orlannumber_to'),)


class Orlangprslist(models.Model):
    pairnumber = models.SmallIntegerField(db_column='PairNumber', primary_key=True)  # Field name made lowercase. The composite primary key (PairNumber, OrlanNumber) found, that is not supported. The first column is selected.
    orlannumber = models.SmallIntegerField(db_column='OrlanNumber')  # Field name made lowercase.
    vpnname = models.CharField(db_column='VPNName', max_length=50, blank=True, null=True)  # Field name made lowercase.
    ip = models.CharField(db_column='IP', max_length=15, blank=True, null=True)  # Field name made lowercase.
    port = models.CharField(db_column='Port', max_length=6, blank=True, null=True)  # Field name made lowercase.
    connectionname = models.CharField(db_column='ConnectionName', max_length=50, blank=True, null=True)  # Field name made lowercase.
    comport = models.CharField(db_column='COMPort', max_length=5, blank=True, null=True)  # Field name made lowercase.
    enablecontrolconnection = models.BooleanField(db_column='EnableControlConnection')  # Field name made lowercase.
    enablecontrolpower = models.BooleanField(db_column='EnableControlPower')  # Field name made lowercase.
    periodchecking = models.DateTimeField(db_column='PeriodChecking', blank=True, null=True)  # Field name made lowercase.
    disconnectonrun = models.BooleanField(db_column='DisconnectOnRun')  # Field name made lowercase.
    disconnectonexit = models.BooleanField(db_column='DisconnectOnExit')  # Field name made lowercase.
    videoorlan = models.BooleanField(db_column='VideoOrlan')  # Field name made lowercase.
    computername = models.CharField(db_column='ComputerName', max_length=70, blank=True, null=True)  # Field name made lowercase.
    enablelogging = models.BooleanField(db_column='EnableLogging')  # Field name made lowercase.
    signallevel = models.SmallIntegerField(db_column='SignalLevel', blank=True, null=True)  # Field name made lowercase.
    signalleveldate = models.DateTimeField(db_column='SignalLevelDate', blank=True, null=True)  # Field name made lowercase.
    vpn = models.ForeignKey('Vpns', models.DO_NOTHING)
    ftpip = models.CharField(db_column='FtpIp', max_length=15, blank=True, null=True)  # Field name made lowercase.
    ftpport = models.CharField(db_column='FtpPort', max_length=5, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'OrlanGPRSList'
        unique_together = (('pairnumber', 'orlannumber'),)


class Orlanlist(models.Model):
    busnumber = models.SmallIntegerField(db_column='BusNumber', primary_key=True)  # Field name made lowercase. The composite primary key (BusNumber, OrlanNumber) found, that is not supported. The first column is selected.
    orlannumber = models.SmallIntegerField(db_column='OrlanNumber')  # Field name made lowercase.
    mobileno = models.CharField(db_column='MobileNo', unique=True, max_length=15)  # Field name made lowercase.
    mobileforstate = models.CharField(db_column='MobileForState', unique=True, max_length=15)  # Field name made lowercase.
    lastevent = models.DateTimeField(db_column='LastEvent', blank=True, null=True)  # Field name made lowercase.
    lastcheck = models.DateTimeField(db_column='LastCheck', blank=True, null=True)  # Field name made lowercase.
    checkperiod = models.DateTimeField(db_column='CheckPeriod')  # Field name made lowercase.
    numberoftry = models.SmallIntegerField(db_column='NumberOfTry')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'OrlanList'
        unique_together = (('busnumber', 'orlannumber'),)


class Panel(models.Model):
    panel_id = models.CharField(db_column='Panel_id', primary_key=True, max_length=15, db_comment='Номер объекта')  # Field name made lowercase.
    password_field = models.CharField(db_column='Password_', max_length=12, blank=True, null=True, db_comment='Пароль')  # Field name made lowercase. Field renamed because it ended with '_'.
    createdate = models.DateTimeField(db_column='CreateDate', blank=True, null=True, db_comment='Дата создания')  # Field name made lowercase.
    disabled = models.BooleanField(db_column='Disabled', db_comment='1 - Объект отключен')  # Field name made lowercase.
    remarks = models.CharField(db_column='Remarks', max_length=100, blank=True, null=True, db_comment='Тип сигнализации')  # Field name made lowercase.
    computer = models.CharField(max_length=50, blank=True, null=True, db_comment='Имя компьютера, на котором изм')
    datelastchange = models.DateTimeField(db_column='DateLastChange', blank=True, null=True, db_comment='Дата последнего изменения данн')  # Field name made lowercase.
    engineer_id = models.IntegerField(blank=True, null=True, db_comment='engineers.engineer_id')
    area = models.ForeignKey(Areas, models.DO_NOTHING, db_column='Area_id', blank=True, null=True, db_comment='Areas.Area_id')  # Field name made lowercase.
    additionaltechnicalinformation = models.CharField(db_column='AdditionalTechnicalInformation', max_length=2000, blank=True, null=True, db_comment='Дополнительная техническая инф')  # Field name made lowercase.
    onetestequalall = models.BooleanField(db_column='OneTestEqualAll', db_comment='Приход теста от любого прибора')  # Field name made lowercase.
    master = models.ForeignKey(Masters, models.DO_NOTHING, blank=True, null=True, db_comment='Masters.Master_id')
    installer = models.ForeignKey(Installers, models.DO_NOTHING, blank=True, null=True, db_comment='Installers.Installer_id')
    compediting = models.CharField(db_column='CompEditing', max_length=20, blank=True, null=True, db_comment='Имя компьютера, на котором дан')  # Field name made lowercase.
    testpanel = models.BooleanField(db_column='TestPanel', db_comment='1 - Постоянный стенд')  # Field name made lowercase.
    partial = models.CharField(db_column='Partial', max_length=500, blank=True, null=True, db_comment='Частичные отключения')  # Field name made lowercase.
    latitude = models.CharField(db_column='Latitude', max_length=20, blank=True, null=True, db_comment='GPS координаты - Широта')  # Field name made lowercase.
    longtitude = models.CharField(db_column='Longtitude', max_length=20, blank=True, null=True, db_comment='GPS координаты - Долгота')  # Field name made lowercase.
    isgpsconfirm = models.BooleanField(db_column='isGPSConfirm', db_comment='GPS координаты подтверждены')  # Field name made lowercase.
    complasteditgps = models.CharField(db_column='CompLastEditGPS', max_length=70, blank=True, null=True, db_comment='Имя компьютера, на котором изм')  # Field name made lowercase.
    engine = models.BooleanField(db_column='Engine', db_comment='Для подвижного объекта состоян')  # Field name made lowercase.
    track = models.IntegerField(db_column='Track', db_comment='vwPanelMobileGPS.TrackID')  # Field name made lowercase.
    isalwayssendgps = models.BooleanField(db_column='isAlwaysSendGPS', db_comment='Объект постоянно шлет GPS коор')  # Field name made lowercase.
    movable_object = models.BooleanField(db_column='Movable_Object', db_comment='1 - подвижный объект')  # Field name made lowercase.
    panel_type = models.SmallIntegerField(db_column='Panel_type', db_comment='1 - пожарный объект')  # Field name made lowercase.
    pult_id = models.IntegerField(db_column='Pult_id', blank=True, null=True, db_comment='Pults.Pult_id')  # Field name made lowercase.
    username = models.CharField(db_column='UserName', max_length=200, blank=True, null=True, db_comment='Имя пользователя, который изме')  # Field name made lowercase.
    regionid = models.IntegerField(db_column='RegionID', blank=True, null=True, db_comment='RegionsTable.RegionID')  # Field name made lowercase.
    iscontactidredirect = models.BooleanField(db_column='IsContactIDRedirect')  # Field name made lowercase.
    contactidobjectnumber = models.CharField(db_column='ContactIDObjectNumber', max_length=15, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Panel'
        db_table_comment = 'Объекты'


class PanelTracking(models.Model):
    panel = models.OneToOneField(Panel, models.DO_NOTHING, db_column='Panel_id', primary_key=True, db_comment='Panel.Panel_id')  # Field name made lowercase. The composite primary key (Panel_id, Tracking_id) found, that is not supported. The first column is selected.
    tracking = models.ForeignKey('Tracking', models.DO_NOTHING, db_column='Tracking_id', db_comment='Tracking.Tracking_id')  # Field name made lowercase.
    trackingdate = models.DateTimeField(db_column='TrackingDate', blank=True, null=True, db_comment='Дата')  # Field name made lowercase.
    trackidpostponed = models.IntegerField(db_column='TrackIdPostponed')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Panel_Tracking'
        unique_together = (('panel', 'tracking'),)
        db_table_comment = 'Напоминания о заменах на объек'


class Personpermitongrrespcategory(models.Model):
    id = models.AutoField(db_column='ID')  # Field name made lowercase.
    person = models.OneToOneField('Personal', models.DO_NOTHING, db_column='Person_ID', primary_key=True)  # Field name made lowercase. The composite primary key (Person_ID, GroupRespCategory_ID) found, that is not supported. The first column is selected.
    grouprespcategory = models.ForeignKey(Groupresponsecategory, models.DO_NOTHING, db_column='GroupRespCategory_ID')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'PersonPermitOnGrRespCategory'
        unique_together = (('person', 'grouprespcategory'),)


class PersonAuth(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    person_login = models.ForeignKey('Personal', models.DO_NOTHING, db_column='Person_Login', to_field='Person_Login')  # Field name made lowercase.
    computer = models.CharField(db_column='Computer', max_length=70)  # Field name made lowercase.
    program = models.CharField(db_column='Program', max_length=50)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Person_Auth'
        unique_together = (('person_login', 'computer', 'program'),)


class PersonPermissions(models.Model):
    person = models.OneToOneField('Personal', models.DO_NOTHING, db_column='Person_Id', primary_key=True, db_comment='ID')  # Field name made lowercase.
    caneditdb = models.BooleanField(db_column='CanEditDB', db_comment='Редактирование базы данных')  # Field name made lowercase.
    canprocessevent = models.BooleanField(db_column='CanProcessEvent', db_comment='Прием событий')  # Field name made lowercase.
    canstands = models.BooleanField(db_column='CanStands', db_comment='Добавление объекта в стенды')  # Field name made lowercase.
    canremotereport = models.BooleanField(db_column='CanRemoteReport', db_comment='Отчет снятия запрета')  # Field name made lowercase.
    canremotearmed = models.BooleanField(db_column='CanRemoteArmed', db_comment='Удаленная постановка под охран')  # Field name made lowercase.
    canremoteaux = models.BooleanField(db_column='CanRemoteAUX', db_comment='Выключение AUX')  # Field name made lowercase.
    canremotebanguarding = models.BooleanField(db_column='CanRemoteBanGuarding', db_comment='Запрет постановки')  # Field name made lowercase.
    canremotesignallvl = models.BooleanField(db_column='CanRemoteSignalLvl', db_comment='Запрос уровня сигнала')  # Field name made lowercase.
    canremoteelcount = models.BooleanField(db_column='CanRemoteElCount', db_comment='Запрос показаний электросчетчи')  # Field name made lowercase.
    canremotereset = models.BooleanField(db_column='CanRemoteReset', db_comment='Выполнять команду "Сброс"')  # Field name made lowercase.
    canremotereleoperations = models.BooleanField(db_column='CanRemoteReleOperations', db_comment='Операции вкл./выкл. реле')  # Field name made lowercase.
    canaddstolenkey = models.BooleanField(db_column='CanAddStolenKey', db_comment='Добавление запрещенных ключей')  # Field name made lowercase.
    canremovestolenkey = models.BooleanField(db_column='CanRemoveStolenKey', db_comment='Удаление запрещенных ключей')  # Field name made lowercase.
    canremoteupdate = models.BooleanField(db_column='CanRemoteUpdate', db_comment='Дистанционное обновление прибо')  # Field name made lowercase.
    canchangesim = models.BooleanField(db_column='CanChangeSim', db_comment='Смена Sim')  # Field name made lowercase.
    canremotevideo = models.BooleanField(db_column='CanRemoteVideo', db_comment='Управление Лунь-Видео')  # Field name made lowercase.
    cangpscommand = models.BooleanField(db_column='CanGPSCommand', db_comment='Управление Алет')  # Field name made lowercase.
    caneditgpsdata = models.BooleanField(db_column='CanEditGPSData', db_comment='Редактировать GPS координаты')  # Field name made lowercase.
    cancancelalarmbutton = models.BooleanField(db_column='CanCancelAlarmButton')  # Field name made lowercase.
    canchangegrrespcategory = models.BooleanField(db_column='CanChangeGrRespCategory')  # Field name made lowercase.
    canviewsettings = models.BooleanField(db_column='CanViewSettings')  # Field name made lowercase.
    caneditsettings = models.BooleanField(db_column='CanEditSettings')  # Field name made lowercase.
    canaddtoignoredstands = models.BooleanField(db_column='CanAddToIgnoredStands', db_comment='Добавление объекта в игнорируе')  # Field name made lowercase.
    canremotearmedlun11 = models.BooleanField(db_column='CanRemoteArmedLun11')  # Field name made lowercase.
    canremotedisarmed = models.BooleanField(db_column='CanRemoteDisarmed')  # Field name made lowercase.
    canbulkchanges = models.BooleanField(db_column='CanBulkChanges')  # Field name made lowercase.
    cancommentjournalresponsegroup = models.BooleanField(db_column='CanCommentJournalResponseGroup')  # Field name made lowercase.
    canprintjournalresponsegroup = models.BooleanField(db_column='CanPrintJournalResponseGroup')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Person_Permissions'
        db_table_comment = 'Разрешения персонала'


class PersonRole(models.Model):
    role_id = models.IntegerField(db_column='Role_ID', primary_key=True, db_comment='ID')  # Field name made lowercase.
    role_name = models.CharField(db_column='Role_Name', max_length=50, blank=True, null=True, db_comment='Должность')  # Field name made lowercase.
    message = models.CharField(db_column='Message', max_length=500, blank=True, null=True, db_comment='Описание')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Person_Role'
        db_table_comment = 'Должности'


class Personal(models.Model):
    person_id = models.AutoField(db_column='Person_Id', primary_key=True, db_comment='ID')  # Field name made lowercase.
    person_name = models.CharField(db_column='Person_Name', max_length=200, blank=True, null=True, db_comment='ФИО сотрудника')  # Field name made lowercase.
    person_role = models.ForeignKey(PersonRole, models.DO_NOTHING, db_column='Person_Role_id', db_comment='Person_Role.Role_ID')  # Field name made lowercase.
    person_login = models.CharField(db_column='Person_Login', unique=True, max_length=15, db_comment='Логин')  # Field name made lowercase.
    person_psw = models.CharField(db_column='Person_Psw', max_length=50, db_comment='Пароль')  # Field name made lowercase.
    work_status = models.BooleanField(db_column='Work_Status', blank=True, null=True, db_comment='Пользователь залогинен: 1 - да')  # Field name made lowercase.
    computer = models.CharField(db_column='Computer', max_length=70, blank=True, null=True, db_comment='Имя компьютера, на котором зал')  # Field name made lowercase.
    deleted = models.BooleanField(db_column='Deleted', db_comment='Запись удалена: 1 - да; 0 - не')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Personal'
        db_table_comment = 'Персонал'


class Portsettings(models.Model):
    field = models.CharField(db_column='Field', max_length=250)  # Field name made lowercase.
    value = models.IntegerField(db_column='Value')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'PortSettings'


class Pultbindperson(models.Model):
    bind_id = models.AutoField()
    person_id = models.IntegerField()
    pult_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'PultBindPerson'
        unique_together = (('person_id', 'pult_id'),)


class Pults(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    pult_name = models.CharField(db_column='Pult_Name', unique=True, max_length=500, blank=True, null=True)  # Field name made lowercase.
    pult_director = models.CharField(db_column='Pult_Director', max_length=300, blank=True, null=True)  # Field name made lowercase.
    pult_adres = models.CharField(db_column='Pult_Adres', max_length=300, blank=True, null=True)  # Field name made lowercase.
    pult_phone = models.CharField(db_column='Pult_Phone', max_length=500, blank=True, null=True)  # Field name made lowercase.
    pult_description = models.CharField(db_column='Pult_Description', max_length=1000, blank=True, null=True)  # Field name made lowercase.
    pult_idnumber = models.CharField(db_column='Pult_IDNumber', max_length=50, blank=True, null=True)  # Field name made lowercase.
    res_name = models.CharField(db_column='RES_Name', max_length=300, blank=True, null=True)  # Field name made lowercase.
    res_address = models.CharField(db_column='RES_Address', max_length=300, blank=True, null=True)  # Field name made lowercase.
    res_phone = models.CharField(db_column='RES_Phone', max_length=300, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Pults'


class Radiozonetype(models.Model):
    typeid = models.IntegerField(db_column='typeId', primary_key=True)  # Field name made lowercase.
    typename = models.CharField(db_column='typeName', max_length=15)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'RadioZoneType'


class Receivedpackages(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    orlannumber = models.IntegerField(db_column='OrlanNumber')  # Field name made lowercase.
    orlanpairnumber = models.IntegerField(db_column='OrlanPairNumber')  # Field name made lowercase.
    receivedtime = models.DateTimeField(db_column='ReceivedTime')  # Field name made lowercase.
    line = models.CharField(db_column='Line', max_length=10)  # Field name made lowercase.
    package = models.CharField(db_column='Package', max_length=2000)  # Field name made lowercase.
    remoteip = models.CharField(db_column='RemoteIp', max_length=25)  # Field name made lowercase.
    remoteport = models.IntegerField(db_column='RemotePort')  # Field name made lowercase.
    cpid = models.CharField(db_column='CpId', max_length=16, blank=True, null=True)  # Field name made lowercase.
    state = models.BooleanField(db_column='State', blank=True, null=True)  # Field name made lowercase.
    compname = models.CharField(db_column='CompName', max_length=20)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ReceivedPackages'


class Regionstable(models.Model):
    regionid = models.AutoField(db_column='RegionID', primary_key=True)  # Field name made lowercase.
    regionnum = models.CharField(db_column='RegionNum', unique=True, max_length=50)  # Field name made lowercase.
    regionname = models.CharField(db_column='RegionName', max_length=100)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'RegionsTable'


class Remarks(models.Model):
    remarks_id = models.AutoField(db_column='Remarks_id', primary_key=True, db_comment='ID')  # Field name made lowercase.
    panel = models.ForeignKey(Groups, models.DO_NOTHING, db_comment='Groups.Panel_id')
    group = models.ForeignKey(Groups, models.DO_NOTHING, related_name='remarks_group_set', blank=True, null=True, db_comment='Groups.Group_')
    message = models.CharField(max_length=300, blank=True, null=True, db_comment='Текст примечания')
    endtime = models.DateTimeField(db_column='EndTime', blank=True, null=True, db_comment='Конечная дата действия примеча')  # Field name made lowercase.
    remarkno = models.IntegerField(db_column='RemarkNo', db_comment='Порядковый номер примечания')  # Field name made lowercase.
    autodel = models.BooleanField(blank=True, null=True, db_comment='1 - временное примечание')

    class Meta:
        managed = False
        db_table = 'Remarks'
        db_table_comment = 'Примечания'


class Replaces(models.Model):
    replace_id = models.AutoField(db_column='Replace_id', primary_key=True, db_comment='ID')  # Field name made lowercase.
    description = models.CharField(db_column='Description', max_length=200, blank=True, null=True, db_comment='Описание замены')  # Field name made lowercase.
    replace_date = models.DateTimeField(db_column='Replace_Date', blank=True, null=True, db_comment='Дата замены')  # Field name made lowercase.
    panel = models.ForeignKey(Panel, models.DO_NOTHING, db_column='Panel_id', blank=True, null=True, db_comment='Panel.Panel_id')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Replaces'
        db_table_comment = 'Замены'


class Requests(models.Model):
    request_id = models.AutoField(db_column='Request_id', primary_key=True)  # Field name made lowercase.
    panel_id = models.CharField(max_length=15)
    vaittime = models.DateTimeField(db_column='VaitTime')  # Field name made lowercase.
    command = models.SmallIntegerField(blank=True, null=True)
    group_field = models.IntegerField(db_column='Group_', blank=True, null=True)  # Field name made lowercase. Field renamed because it ended with '_'.
    computername = models.CharField(db_column='ComputerName', max_length=70)  # Field name made lowercase.
    zone = models.IntegerField(db_column='Zone', blank=True, null=True)  # Field name made lowercase.
    description = models.CharField(db_column='Description', max_length=200, blank=True, null=True)  # Field name made lowercase.
    donestate = models.IntegerField(db_column='DoneState', blank=True, null=True)  # Field name made lowercase.
    owner = models.IntegerField(db_column='Owner')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Requests'


class Responsibleemail(models.Model):
    responsibleemail_id = models.AutoField(db_column='ResponsibleEmail_id', primary_key=True)  # Field name made lowercase.
    responsibleslist = models.ForeignKey('Responsibleslist', models.DO_NOTHING, db_column='ResponsiblesList_id')  # Field name made lowercase.
    emailaddr = models.CharField(db_column='EmailAddr', unique=True, max_length=250)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ResponsibleEmail'


class Responsibletel(models.Model):
    phoneno = models.CharField(db_column='PhoneNo', max_length=25, db_comment='Номер телефона')  # Field name made lowercase.
    typetel = models.ForeignKey('Responsibletypetel', models.DO_NOTHING, db_column='TypeTel_id', blank=True, null=True, db_comment='ResponsibleTypeTel.TypeTel_id')  # Field name made lowercase.
    responsibleslist = models.ForeignKey('Responsibleslist', models.DO_NOTHING, db_column='ResponsiblesList_id')  # Field name made lowercase.
    responsibletel_id = models.AutoField(db_column='ResponsibleTel_id', primary_key=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ResponsibleTel'
        db_table_comment = 'Список телефонов ответственног'


class Responsibleteldescription(models.Model):
    responsible = models.OneToOneField('Responsibles', models.DO_NOTHING, db_column='Responsible_id', primary_key=True)  # Field name made lowercase. The composite primary key (Responsible_id, ResponsibleTel_id) found, that is not supported. The first column is selected.
    responsibletel = models.ForeignKey(Responsibletel, models.DO_NOTHING, db_column='ResponsibleTel_id')  # Field name made lowercase.
    description = models.CharField(db_column='Description', max_length=100, blank=True, null=True)  # Field name made lowercase.
    firealarm = models.BooleanField(db_column='FireAlarm', blank=True, null=True)  # Field name made lowercase.
    clientinfosms = models.BooleanField(db_column='ClientInfoSms', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ResponsibleTelDescription'
        unique_together = (('responsible', 'responsibletel'),)


class Responsibletypetel(models.Model):
    typetel_id = models.SmallAutoField(db_column='TypeTel_id', primary_key=True, db_comment='ID')  # Field name made lowercase.
    typetel = models.CharField(db_column='TypeTel', max_length=50, db_comment='Тип телефона')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ResponsibleTypeTel'
        db_table_comment = 'Типы телефонов'


class Responsibles(models.Model):
    responsible_id = models.AutoField(db_column='Responsible_id', primary_key=True, db_comment='ID')  # Field name made lowercase.
    panel = models.ForeignKey(Groups, models.DO_NOTHING, db_comment='Groups.Panel_id')
    group_field = models.ForeignKey(Groups, models.DO_NOTHING, db_column='Group_', related_name='responsibles_group_field_set', db_comment='Groups.Group_')  # Field name made lowercase. Field renamed because it ended with '_'.
    responsible_number = models.IntegerField(db_column='Responsible_Number', db_comment='Порядковый номер')  # Field name made lowercase.
    responsibleslist = models.ForeignKey('Responsibleslist', models.DO_NOTHING, db_column='ResponsiblesList_id')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Responsibles'
        unique_together = (('panel', 'group_field', 'responsibleslist'),)
        db_table_comment = 'Ответственные лица'


class Responsibleslist(models.Model):
    responsibleslist_id = models.AutoField(db_column='ResponsiblesList_id', primary_key=True)  # Field name made lowercase.
    responsible_name = models.CharField(db_column='Responsible_Name', max_length=100)  # Field name made lowercase.
    responsible_address = models.CharField(db_column='Responsible_Address', max_length=500, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ResponsiblesList'


class ResponsiblesTelBackupTbl(models.Model):
    responsible_id = models.IntegerField(db_column='Responsible_id')  # Field name made lowercase.
    phoneno = models.CharField(db_column='PhoneNo', max_length=25)  # Field name made lowercase.
    typetel_id = models.SmallIntegerField(db_column='TypeTel_id', blank=True, null=True)  # Field name made lowercase.
    description = models.CharField(db_column='Description', max_length=100, blank=True, null=True)  # Field name made lowercase.
    firealarm = models.BooleanField(db_column='FireAlarm', blank=True, null=True)  # Field name made lowercase.
    clientinfosms = models.BooleanField(db_column='ClientInfoSms')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Responsibles_Tel_backup_tbl'


class ResponsiblesBackupTbl(models.Model):
    responsible_id = models.IntegerField(db_column='Responsible_id')  # Field name made lowercase.
    panel_id = models.CharField(max_length=15)
    group_field = models.IntegerField(db_column='Group_')  # Field name made lowercase. Field renamed because it ended with '_'.
    responsible_name = models.CharField(db_column='Responsible_Name', max_length=100, blank=True, null=True)  # Field name made lowercase.
    responsible_number = models.IntegerField(db_column='Responsible_Number')  # Field name made lowercase.
    responsible_adress = models.CharField(db_column='Responsible_Adress', max_length=1000, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Responsibles_backup_tbl'


class Results(models.Model):
    result_id = models.AutoField(db_column='Result_id', primary_key=True)  # Field name made lowercase.
    message = models.CharField(unique=True, max_length=300)
    isuser = models.BooleanField(db_column='isUser', blank=True, null=True)  # Field name made lowercase.
    order = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Results'


class Smslog(models.Model):
    sms_id = models.AutoField(db_column='SMS_id', primary_key=True)  # Field name made lowercase.
    mobileno = models.CharField(db_column='MobileNo', max_length=15)  # Field name made lowercase.
    textsms = models.CharField(db_column='textSMS', max_length=160)  # Field name made lowercase.
    timeadded = models.DateTimeField(db_column='timeAdded', blank=True, null=True)  # Field name made lowercase.
    timesend = models.DateTimeField(db_column='timeSend', blank=True, null=True)  # Field name made lowercase.
    result = models.BooleanField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'SMSLog'


class Serviceorganization(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    servicename = models.CharField(db_column='ServiceName', unique=True, max_length=500)  # Field name made lowercase.
    idcode = models.CharField(db_column='IDCode', max_length=50, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ServiceOrganization'


class Sims(models.Model):
    sim_id = models.AutoField(db_column='SIM_id', primary_key=True, db_comment='ID')  # Field name made lowercase.
    operator = models.ForeignKey(Operators, models.DO_NOTHING, db_column='Operator_id', blank=True, null=True, db_comment='Operators.Operator_id')  # Field name made lowercase.
    vauchload = models.DateTimeField(db_column='VauchLoad', blank=True, null=True, db_comment='Напоминать о пополнении счета')  # Field name made lowercase.
    mphone = models.ForeignKey(Mphone, models.DO_NOTHING, db_column='Mphone_id', blank=True, null=True, db_comment='MPhone.Mphone_id')  # Field name made lowercase.
    simnumber = models.CharField(db_column='SimNumber', unique=True, max_length=13, blank=True, null=True, db_comment='Телефон ППК-Лунь')  # Field name made lowercase.
    simnumberfull = models.CharField(db_column='SimNumberFull', max_length=50, blank=True, null=True, db_comment='Телефон ППК-Лунь с кодом')  # Field name made lowercase.
    mainsim = models.BooleanField(db_column='MainSim', db_comment='1 - основная; 0 - резервная')  # Field name made lowercase.
    bus = models.ForeignKey(Orlanbuses, models.DO_NOTHING, db_column='Bus_id', blank=True, null=True, db_comment='OrlanBuses.Bus_number')  # Field name made lowercase.
    orlangprspairnumber = models.SmallIntegerField(db_column='OrlanGPRSPairNumber', blank=True, null=True, db_comment='Номер пары GPRS орланов, на ко')  # Field name made lowercase.
    orlanvideopairnumber = models.SmallIntegerField(db_column='OrlanVideoPairNumber', blank=True, null=True, db_comment='Номер пары видео-орланов, на к')  # Field name made lowercase.
    networktype = models.SmallIntegerField(db_column='NetworkType', blank=True, null=True)  # Field name made lowercase.
    openinternetnumber = models.IntegerField(db_column='OpenInternetNumber', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Sims'
        db_table_comment = 'SIM карточки'


class Sosaccessevents(models.Model):
    event_id = models.IntegerField(db_column='Event_id', primary_key=True)  # Field name made lowercase.
    panel_id = models.CharField(db_column='Panel_id', max_length=15)  # Field name made lowercase.
    group_field = models.IntegerField(db_column='Group_')  # Field name made lowercase. Field renamed because it ended with '_'.
    zone = models.IntegerField(db_column='Zone', blank=True, null=True)  # Field name made lowercase.
    idtcode = models.SmallIntegerField(db_column='idTCode')  # Field name made lowercase.
    code = models.CharField(db_column='Code', max_length=6)  # Field name made lowercase.
    codemessage = models.CharField(db_column='CodeMessage', max_length=500)  # Field name made lowercase.
    timeevent = models.DateTimeField(db_column='TimeEvent')  # Field name made lowercase.
    result = models.SmallIntegerField(blank=True, null=True)
    groupmessage = models.CharField(db_column='GroupMessage', max_length=150, blank=True, null=True)  # Field name made lowercase.
    zonemessage = models.CharField(db_column='ZoneMessage', max_length=250, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'SosAccessEvents'


class Stands(models.Model):
    panel_id = models.CharField(db_column='Panel_id', max_length=15, db_comment='Groups.Panel_id')  # Field name made lowercase.
    group_field = models.IntegerField(db_column='Group_', blank=True, null=True, db_comment='Groups.Group_')  # Field name made lowercase. Field renamed because it ended with '_'.
    zone = models.IntegerField(db_column='Zone', blank=True, null=True, db_comment='Шлейф')  # Field name made lowercase.
    timebegin = models.DateTimeField(db_column='TimeBegin', blank=True, null=True, db_comment='Начальное время')  # Field name made lowercase.
    timeend = models.DateTimeField(db_column='TimeEnd', blank=True, null=True, db_comment='Конечное время')  # Field name made lowercase.
    type_stand = models.BooleanField(db_column='Type_Stand', blank=True, null=True, db_comment='0 - временный; 1 - постоянный')  # Field name made lowercase.
    standorkey = models.SmallIntegerField(blank=True, null=True, db_comment='0 - стенд; 1- запрещенный ключ')
    engineer = models.ForeignKey('Engineers', models.DO_NOTHING, db_column='Engineer_id', blank=True, null=True, db_comment='engineers.engineer_id')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Stands'
        db_table_comment = 'Стенды/Запрещенные ключи/Игнор'


class States(models.Model):
    state_id = models.AutoField(db_column='State_id', primary_key=True, db_comment='ID')  # Field name made lowercase.
    statename = models.CharField(db_column='StateName', max_length=60, db_comment='Наименование')  # Field name made lowercase.
    isoverprocess = models.BooleanField(db_column='isOverProcess', db_comment='1 - завершение обработки')  # Field name made lowercase.
    ischangestateevent = models.BooleanField(db_column='IsChangeStateEvent', db_comment='1 - изменение состояния')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'States'
        db_table_comment = 'Список доступных операций для '


class Statusgroupresponse(models.Model):
    status_id = models.AutoField(primary_key=True, db_comment='ID')
    status = models.IntegerField(blank=True, null=True, db_comment='Дополнительный статус группы: ')
    reason = models.CharField(max_length=150, blank=True, null=True, db_comment='Описание')
    issystem = models.BooleanField(db_column='IsSystem', db_comment='Системное состояние: 1 - да; 0')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'StatusGroupResponse'
        db_table_comment = 'Состояния групп реагирования'


class Temp(models.Model):
    event_id = models.IntegerField(db_column='Event_id', primary_key=True)  # Field name made lowercase.
    panel_id = models.CharField(db_column='Panel_id', max_length=15, blank=True, null=True)  # Field name made lowercase.
    group_field = models.IntegerField(db_column='Group_', blank=True, null=True)  # Field name made lowercase. Field renamed because it ended with '_'.
    line = models.CharField(db_column='Line', max_length=10, blank=True, null=True)  # Field name made lowercase.
    zone = models.IntegerField(db_column='Zone', blank=True, null=True)  # Field name made lowercase.
    code = models.CharField(db_column='Code', max_length=6, blank=True, null=True)  # Field name made lowercase.
    codegroup = models.SmallIntegerField(db_column='CodeGroup', blank=True, null=True)  # Field name made lowercase.
    timeevent = models.DateTimeField(db_column='TimeEvent', blank=True, null=True)  # Field name made lowercase.
    receiver = models.IntegerField(db_column='Receiver', blank=True, null=True)  # Field name made lowercase.
    phone = models.CharField(db_column='Phone', max_length=15, blank=True, null=True)  # Field name made lowercase.
    metercount = models.CharField(db_column='MeterCount', max_length=300, blank=True, null=True)  # Field name made lowercase.
    stateevent = models.SmallIntegerField(db_column='StateEvent', blank=True, null=True)  # Field name made lowercase.
    event_parent = models.ForeignKey('self', models.DO_NOTHING, db_column='Event_Parent_id', blank=True, null=True)  # Field name made lowercase.
    date_key = models.IntegerField(db_column='Date_Key')  # Field name made lowercase.
    priority = models.IntegerField(db_column='Priority', blank=True, null=True)  # Field name made lowercase.
    computer = models.CharField(db_column='Computer', max_length=250, blank=True, null=True)  # Field name made lowercase.
    bitmask = models.IntegerField(db_column='BitMask')  # Field name made lowercase.
    deviceeventtime = models.DateTimeField(db_column='DeviceEventTime', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Temp'


class Templates(models.Model):
    template_name = models.CharField(db_column='Template_Name', unique=True, max_length=500)  # Field name made lowercase.
    panel_id = models.CharField(db_column='Panel_id', primary_key=True, max_length=15)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Templates'


class Timers(models.Model):
    timer_id = models.AutoField(db_column='Timer_id', primary_key=True)  # Field name made lowercase.
    panel_id = models.CharField(db_column='Panel_id', max_length=15)  # Field name made lowercase.
    group_field = models.IntegerField(db_column='Group_')  # Field name made lowercase. Field renamed because it ended with '_'.
    lurking = models.ForeignKey(Lurking, models.DO_NOTHING, db_column='Lurking_id')  # Field name made lowercase.
    timeelapse = models.DateTimeField(db_column='TimeElapse')  # Field name made lowercase.
    grresponse_id = models.IntegerField(db_column='GrResponse_id', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Timers'


class Tracking(models.Model):
    tracking_id = models.AutoField(db_column='Tracking_id', primary_key=True, db_comment='ID')  # Field name made lowercase.
    name_tracking = models.CharField(db_column='Name_Tracking', max_length=100, blank=True, null=True, db_comment='Описание')  # Field name made lowercase.
    defaultincrementtracking = models.SmallIntegerField(db_column='DefaultIncrementTracking', blank=True, null=True, db_comment='Через сколько истекает')  # Field name made lowercase.
    defaultincrementtypeperiod = models.SmallIntegerField(db_column='DefaultIncrementTypePeriod', blank=True, null=True, db_comment='Единица измерения: 0 - год; 1 ')  # Field name made lowercase.
    deafultperiodbeforedatetracking = models.SmallIntegerField(db_column='DeafultPeriodBeforeDateTracking', blank=True, null=True, db_comment='Через сколько попадает в списо')  # Field name made lowercase.
    defaulttypeperiod = models.SmallIntegerField(db_column='DefaultTypePeriod', blank=True, null=True, db_comment='Единица измерения: 0 - год; 1 ')  # Field name made lowercase.
    issystem = models.BooleanField(db_column='IsSystem', blank=True, null=True, db_comment='1 - напоминание добавляется ав')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Tracking'
        db_table_comment = 'Напоминания о заменах'


class Typecode(models.Model):
    idtcode = models.IntegerField(db_column='idTCode', primary_key=True)  # Field name made lowercase.
    message = models.CharField(db_column='Message', unique=True, max_length=50)  # Field name made lowercase.
    priority = models.SmallIntegerField(db_column='Priority', blank=True, null=True)  # Field name made lowercase.
    order = models.SmallIntegerField(blank=True, null=True)
    typecodefilename = models.CharField(db_column='TypeCodeFileName', max_length=100, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TypeCode'


class Typedevices(models.Model):
    device_id = models.AutoField(db_column='Device_id', primary_key=True, db_comment='ID')  # Field name made lowercase.
    typedevice = models.CharField(db_column='TypeDevice', unique=True, max_length=200, db_comment='Тип ППК')  # Field name made lowercase.
    usealarmdelay = models.BooleanField(db_column='UseAlarmDelay', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TypeDevices'
        db_table_comment = 'Типы ППК'


class Users(models.Model):
    panel = models.OneToOneField(Groups, models.DO_NOTHING, db_column='Panel_id', primary_key=True, db_comment='Groups.Panel_id')  # Field name made lowercase. The composite primary key (Panel_id, Group_, UserCode) found, that is not supported. The first column is selected.
    group_field = models.ForeignKey(Groups, models.DO_NOTHING, db_column='Group_', related_name='users_group_field_set', db_comment='Groups.Group_')  # Field name made lowercase. Field renamed because it ended with '_'.
    usercode = models.IntegerField(db_column='UserCode', db_comment='Номер кода доступа')  # Field name made lowercase.
    username = models.CharField(db_column='UserName', max_length=200, blank=True, null=True, db_comment='Ф.И.О. владельца кода доступа')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Users'
        unique_together = (('panel', 'group_field', 'usercode'),)
        db_table_comment = 'Ключи доступа'


class Vpns(models.Model):
    vpn_id = models.AutoField(db_column='VPN_id', primary_key=True)  # Field name made lowercase.
    vpn_name = models.CharField(db_column='VPN_Name', unique=True, max_length=100, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'VPNs'


class Videozones(models.Model):
    panel_id = models.CharField(db_column='Panel_id', primary_key=True, max_length=15)  # Field name made lowercase. The composite primary key (Panel_id, VideoZone, Group_) found, that is not supported. The first column is selected.
    videozone = models.IntegerField(db_column='VideoZone')  # Field name made lowercase.
    group_field = models.IntegerField(db_column='Group_')  # Field name made lowercase. Field renamed because it ended with '_'.
    message = models.CharField(db_column='Message', max_length=250, blank=True, null=True)  # Field name made lowercase.
    status = models.IntegerField(db_column='Status', blank=True, null=True)  # Field name made lowercase.
    statustime = models.DateTimeField(db_column='StatusTime', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'VideoZones'
        unique_together = (('panel_id', 'videozone', 'group_field'),)


class Voicerequests(models.Model):
    request_id = models.AutoField(db_column='Request_id', primary_key=True)  # Field name made lowercase.
    mobile = models.CharField(db_column='Mobile', max_length=15)  # Field name made lowercase.
    command = models.SmallIntegerField(db_column='Command')  # Field name made lowercase.
    busnumber = models.SmallIntegerField(db_column='BusNumber')  # Field name made lowercase.
    devicenumber = models.SmallIntegerField(db_column='DeviceNumber')  # Field name made lowercase.
    timeforcommand = models.DateTimeField(db_column='TimeForCommand')  # Field name made lowercase.
    panel_id = models.CharField(max_length=15)
    group_field = models.IntegerField(db_column='Group_', blank=True, null=True)  # Field name made lowercase. Field renamed because it ended with '_'.
    iscsd = models.BooleanField(db_column='isCSD', blank=True, null=True)  # Field name made lowercase.
    deviceid = models.SmallIntegerField(db_column='deviceId', blank=True, null=True)  # Field name made lowercase.
    zone = models.IntegerField(db_column='Zone', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'VoiceRequests'


class Z8Checking(models.Model):
    panel_id = models.CharField(db_column='Panel_id', primary_key=True, max_length=15)  # Field name made lowercase. The composite primary key (Panel_id, Group_) found, that is not supported. The first column is selected.
    group_field = models.IntegerField(db_column='Group_')  # Field name made lowercase. Field renamed because it ended with '_'.
    timeevent = models.DateTimeField(db_column='TimeEvent', blank=True, null=True)  # Field name made lowercase.
    timeend = models.DateTimeField(db_column='TimeEnd', blank=True, null=True)  # Field name made lowercase.
    computer = models.CharField(db_column='Computer', max_length=70, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Z8Checking'
        unique_together = (('panel_id', 'group_field'),)


class Zones(models.Model):
    panel = models.OneToOneField(Groups, models.DO_NOTHING, db_column='Panel_id', primary_key=True, db_comment='Groups.Panel_id')  # Field name made lowercase. The composite primary key (Panel_id, Zone, Group_) found, that is not supported. The first column is selected.
    zone = models.IntegerField(db_column='Zone', db_comment='Номер')  # Field name made lowercase.
    group_field = models.ForeignKey(Groups, models.DO_NOTHING, db_column='Group_', related_name='zones_group_field_set', db_comment='Groups.Group_')  # Field name made lowercase. Field renamed because it ended with '_'.
    message = models.CharField(db_column='Message', max_length=250, blank=True, null=True, db_comment='Описание шлейфа')  # Field name made lowercase.
    status = models.IntegerField(db_column='Status', blank=True, null=True, db_comment='Состояние шлейфа: 1 - норма; 2')  # Field name made lowercase.
    statustime = models.DateTimeField(db_column='StatusTime', blank=True, null=True, db_comment='Дата и время изменения состоян')  # Field name made lowercase.
    ispatrol = models.BooleanField(db_column='IsPatrol', blank=True, null=True, db_comment='Патруль: 1 - да; 0 - нет')  # Field name made lowercase.
    isalarmbutton = models.BooleanField(db_column='IsAlarmButton', blank=True, null=True, db_comment='Тревожная кнопка')  # Field name made lowercase.
    radiozonetypeid = models.ForeignKey(Radiozonetype, models.DO_NOTHING, db_column='RadioZoneTypeid')  # Field name made lowercase.
    ispatrolinspectionsystem = models.BooleanField(db_column='IsPatrolInspectionSystem')  # Field name made lowercase.
    lastpatrolinspection = models.DateTimeField(db_column='LastPatrolInspection', blank=True, null=True)  # Field name made lowercase.
    isviolationpatrolcontrol = models.BooleanField(db_column='IsViolationPatrolControl')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Zones'
        unique_together = (('panel', 'zone', 'group_field'),)
        db_table_comment = 'Шлейфы'


class ZonesGroupresponse(models.Model):
    group = models.OneToOneField(Groupresponse, models.DO_NOTHING, db_column='Group_id', primary_key=True, db_comment='GroupResponse.Group_id')  # Field name made lowercase. The composite primary key (Group_id, Zone) found, that is not supported. The first column is selected.
    zone = models.IntegerField(db_column='Zone', db_comment='Номер шлейфа')  # Field name made lowercase.
    message = models.CharField(db_column='Message', max_length=250, blank=True, null=True, db_comment='Описание шлейфа')  # Field name made lowercase.
    status = models.IntegerField(db_column='Status', blank=True, null=True, db_comment='Состояние шлейфа: 1 - норма; 2')  # Field name made lowercase.
    statustime = models.DateTimeField(db_column='StatusTime', blank=True, null=True, db_comment='Время изменения состояние шлей')  # Field name made lowercase.
    isalarmbutton = models.BooleanField(db_column='IsAlarmButton', db_comment='Тревожная кнопка: 1 - да; 0 - ')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Zones_GroupResponse'
        unique_together = (('group', 'zone'),)
        db_table_comment = 'Список шлейфов и их состояние'


class ZonesIpcameras(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    panel = models.ForeignKey(Zones, models.DO_NOTHING, db_column='Panel_Id', to_field='Zone')  # Field name made lowercase.
    group_field = models.ForeignKey(Zones, models.DO_NOTHING, db_column='Group_', to_field='Zone', related_name='zonesipcameras_group_field_set')  # Field name made lowercase. Field renamed because it ended with '_'.
    zone = models.ForeignKey(Zones, models.DO_NOTHING, db_column='Zone', to_field='Zone', related_name='zonesipcameras_zone_set')  # Field name made lowercase.
    ipcamera = models.ForeignKey(Ipcameras, models.DO_NOTHING, db_column='IPCamera_Id')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Zones_IPCameras'


class AndroidDevice(models.Model):
    device_id = models.AutoField(primary_key=True)
    ip_addr = models.CharField(max_length=15, blank=True, null=True)
    device_descr = models.CharField(unique=True, max_length=16)
    enabled = models.SmallIntegerField()
    ping_time = models.DateTimeField(blank=True, null=True)
    version_id = models.IntegerField(blank=True, null=True)
    device_sign = models.CharField(max_length=50, blank=True, null=True)
    description = models.CharField(db_column='Description', max_length=200, blank=True, null=True)  # Field name made lowercase.
    networktype = models.SmallIntegerField(db_column='NetworkType')  # Field name made lowercase.
    testtimeout = models.DateTimeField(db_column='TestTimeout', blank=True, null=True)  # Field name made lowercase.
    vpn = models.ForeignKey(Vpns, models.DO_NOTHING, db_column='VPN_id')  # Field name made lowercase.
    lossconnectiongenerated = models.BooleanField(db_column='LossConnectionGenerated')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'android_device'


class AndroidDeviceLink(models.Model):
    device = models.ForeignKey(AndroidDevice, models.DO_NOTHING)
    group = models.ForeignKey(Groupresponse, models.DO_NOTHING)
    device_group_id = models.AutoField(primary_key=True)

    class Meta:
        managed = False
        db_table = 'android_device_link'
        unique_together = (('device', 'group'),)


class AndroidGpsRedirect(models.Model):
    event_id = models.IntegerField(primary_key=True)  # The composite primary key (event_id, device_id) found, that is not supported. The first column is selected.
    device = models.ForeignKey(AndroidDevice, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'android_gps_redirect'
        unique_together = (('event_id', 'device'),)


class AndroidHistory(models.Model):
    history_id = models.AutoField(primary_key=True)
    history_time = models.DateTimeField()
    package_id = models.IntegerField()
    direction = models.SmallIntegerField()
    device = models.ForeignKey(AndroidDevice, models.DO_NOTHING)
    event_id = models.IntegerField(blank=True, null=True)
    command = models.CharField(max_length=10)
    description = models.CharField(max_length=100, blank=True, null=True)
    status = models.IntegerField()
    errors = models.CharField(max_length=200, blank=True, null=True)
    sender = models.CharField(max_length=30)
    from_field = models.CharField(db_column='From_', max_length=5)  # Field name made lowercase. Field renamed because it ended with '_'.

    class Meta:
        managed = False
        db_table = 'android_history'


class AndroidUpdateFile(models.Model):
    file_id = models.AutoField(primary_key=True)
    file_name = models.CharField(unique=True, max_length=20)
    sourceid = models.IntegerField()
    version = models.ForeignKey('AndroidVersion', models.DO_NOTHING)
    file_size = models.IntegerField()
    last_modify = models.DateTimeField()
    isdeleted = models.BooleanField()
    panel_id = models.CharField(max_length=15, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'android_update_file'


class AndroidVersion(models.Model):
    version_id = models.IntegerField(primary_key=True)
    version_time = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'android_version'


class Dtproperties(models.Model):
    objectid = models.IntegerField(blank=True, null=True)
    property = models.CharField(max_length=64)
    value = models.CharField(max_length=255, blank=True, null=True)
    uvalue = models.CharField(max_length=255, blank=True, null=True)
    lvalue = models.BinaryField(blank=True, null=True)
    version = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'dtproperties'
        unique_together = (('id', 'property'),)


class Engineers(models.Model):
    engineer_id = models.AutoField(primary_key=True, db_comment='ID')
    engineer_name = models.CharField(unique=True, max_length=200, db_comment='ФИО инженера')
    ip = models.CharField(db_column='IP', max_length=15, blank=True, null=True, db_comment='IP адрес')  # Field name made lowercase.
    work_panel_id = models.CharField(db_column='Work_panel_id', max_length=15, blank=True, null=True, db_comment='Номер объекта в стендах, на ко')  # Field name made lowercase.
    orlanpairnumber = models.SmallIntegerField(db_column='OrlanPairNumber', blank=True, null=True, db_comment='Номер пары GPRS Орланов, на ко')  # Field name made lowercase.
    carpanel = models.ForeignKey(Panel, models.DO_NOTHING, db_column='CarPanel_id', blank=True, null=True, db_comment='Номер объекта машины инженера')  # Field name made lowercase.
    mobileuser = models.ForeignKey(Mobileuser, models.DO_NOTHING, db_column='mobileUser_id', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'engineers'
        db_table_comment = 'Ответственные инженеры'


class Sysdiagrams(models.Model):
    name = models.CharField(max_length=128)
    principal_id = models.IntegerField()
    diagram_id = models.AutoField(primary_key=True)
    version = models.IntegerField(blank=True, null=True)
    definition = models.BinaryField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sysdiagrams'
        unique_together = (('principal_id', 'name'),)


class Videoarchive(models.Model):
    picture_id = models.AutoField(db_column='Picture_id', primary_key=True)  # Field name made lowercase.
    objectid = models.IntegerField(db_column='ObjectId', blank=True, null=True)  # Field name made lowercase.
    videozone = models.IntegerField(db_column='VideoZone', blank=True, null=True)  # Field name made lowercase.
    panel_id = models.CharField(db_column='Panel_id', max_length=15, blank=True, null=True)  # Field name made lowercase.
    result_id = models.IntegerField(db_column='Result_id', blank=True, null=True)  # Field name made lowercase.
    event_id = models.IntegerField(blank=True, null=True)
    timeevent = models.DateTimeField(db_column='TimeEvent', blank=True, null=True)  # Field name made lowercase.
    photo = models.BinaryField(db_column='Photo', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'videoarchive'
