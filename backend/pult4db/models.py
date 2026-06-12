from django.db import models

class Areas(models.Model):
    area_id = models.AutoField(db_column='Area_id', primary_key=True, db_comment='ID')  # Field name made lowercase.
    area_name = models.CharField(db_column='Area_name', unique=True, max_length=200, blank=True, null=True, db_comment='Название района')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Areas'
        db_table_comment = 'Районы'
    
    def __str__(self):
        return f'{self.area_name}'
    
class Channeltypes(models.Model):
    channeltype_id = models.AutoField(db_column='ChannelType_id', primary_key=True, db_comment='ID')  # Field name made lowercase.
    channeltype = models.CharField(db_column='ChannelType', unique=True, max_length=100, blank=True, null=True, db_comment='Режим работы прибора')  # Field name made lowercase.
    priority = models.IntegerField(blank=True, null=True, db_comment='Приоритет')

    class Meta:
        managed = False
        db_table = 'ChannelTypes'
        db_table_comment = 'Типы каналов'

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

    def __str__(self):
        return f'{self.company_id}-{self.companyname}-{self.address}'

class Customers(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    organization = models.CharField(db_column='Organization', max_length=500, blank=True, null=True)  # Field name made lowercase.
    organizationaddress = models.CharField(db_column='OrganizationAddress', max_length=500, blank=True, null=True)  # Field name made lowercase.
    director = models.CharField(db_column='Director', max_length=500, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Customers'

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

class Groupresponsecategory(models.Model):
    categoryid = models.AutoField(db_column='CategoryID', primary_key=True)  # Field name made lowercase.
    description = models.CharField(db_column='Description', unique=True, max_length=100, blank=True, null=True)  # Field name made lowercase.
    sendidcategory = models.IntegerField(db_column='SendIdCategory', unique=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'GroupResponseCategory'

class Groups(models.Model):
    panel = models.OneToOneField('Panel', models.DO_NOTHING, db_column='Panel_id', primary_key=True, db_comment='Panel.Panel_id')  # Field name made lowercase. The composite primary key (Panel_id, Group_) found, that is not supported. The first column is selected.
    group_field = models.IntegerField(db_column='Group_', db_comment='Номер')  # Field name made lowercase. Field renamed because it ended with '_'.
    message = models.CharField(db_column='Message', max_length=100, db_comment='Описание')  # Field name made lowercase.
    isopen = models.BooleanField(db_column='IsOpen', blank=True, null=True, db_comment='Группа под охраной: 0 - да; 1 ')  # Field name made lowercase.
    timeevent = models.DateTimeField(db_column='TimeEvent', blank=True, null=True, db_comment='Время прихода последнего событ')  # Field name made lowercase.
    opencontrol = models.BooleanField(db_column='OpenControl', blank=True, null=True, db_comment='1 - Контроль открытий по распи')  # Field name made lowercase.
    z8timeout = models.DateTimeField(db_column='Z8Timeout', blank=True, null=True, db_comment='Ожидание звонка с объекта при ')  # Field name made lowercase.
    #info = models.ForeignKey('Moreaboutlun7', models.DO_NOTHING, blank=True, null=True, db_comment='MoreAboutLun7.info_id')
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

class Installers(models.Model):
    installer_id = models.AutoField(db_column='Installer_id', primary_key=True, db_comment='ID')  # Field name made lowercase.
    installername = models.CharField(db_column='InstallerName', unique=True, max_length=200, db_comment='ФИО монтажника')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Installers'
        db_table_comment = 'Ответственные монтажники'
    
    def __str__(self):
        return f'{self.installername}'

class Masters(models.Model):
    master_id = models.AutoField(db_column='Master_id', primary_key=True, db_comment='ID')  # Field name made lowercase.
    mastername = models.CharField(db_column='MasterName', unique=True, max_length=200, db_comment='ФИО мастера')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Masters'
        db_table_comment = 'Ответственные мастера'
    
    def __str__(self):
        return f'{self.mastername}'
    
class Mphone(models.Model):
    mphone_id = models.AutoField(db_column='Mphone_id', primary_key=True, db_comment='ID')  # Field name made lowercase.
    panel = models.ForeignKey('Panel', models.DO_NOTHING, db_column='Panel_id', blank=True, null=True, db_comment='Panel.Panel_id')  # Field name made lowercase.
    rstartdate = models.DateTimeField(db_column='RStartDate', blank=True, null=True, db_comment='Дата подключения')  # Field name made lowercase.
    radioversion = models.CharField(db_column='RadioVersion', max_length=50, blank=True, null=True, db_comment='Версия прибора')  # Field name made lowercase.
    #radiotype = models.ForeignKey('Mphoneradiotype', models.DO_NOTHING, db_column='RadioType', blank=True, null=True, db_comment='MphoneRadioType.RadioType_id')  # Field name made lowercase.
    codegroup = models.SmallIntegerField(db_column='CodeGroup', db_comment='Указанный вручную набор кодов')  # Field name made lowercase.
    mainpower = models.BooleanField(db_column='MainPower', blank=True, null=True, db_comment='Основное питание: 1 - есть; 0 ')  # Field name made lowercase.
    backuppower = models.BooleanField(db_column='BackupPower', blank=True, null=True, db_comment='Резервное питание: 1 - есть; 0')  # Field name made lowercase.
    mptime = models.DateTimeField(db_column='MPTime', blank=True, null=True, db_comment='Время последнего изменения сос')  # Field name made lowercase.
    bptime = models.DateTimeField(db_column='BPTime', blank=True, null=True, db_comment='Время последнего изменения сос')  # Field name made lowercase.
    #typetransmitter = models.ForeignKey('Mphonetypetransmitter', models.DO_NOTHING, db_column='TypeTransmitter', blank=True, null=True, db_comment='MphoneTypeTransmitter.TypeTran')  # Field name made lowercase.
    isjablotron = models.BooleanField(db_column='IsJablotron', blank=True, null=True, db_comment='К прибору подключен ППК Jablot')  # Field name made lowercase.
    dot3 = models.BooleanField(db_column='DOT3', blank=True, null=True, db_comment='Использовать короткий протокол')  # Field name made lowercase.
    lasttest = models.DateTimeField(db_column='LastTest', blank=True, null=True, db_comment='Дата и время последнего теста')  # Field name made lowercase.
    lastgprscount = models.IntegerField(db_column='LastGPRSCount', blank=True, null=True, db_comment='Текущий счетчик события')  # Field name made lowercase.
    signallevel = models.SmallIntegerField(db_column='SignalLevel', blank=True, null=True, db_comment='Уровень сигнала')  # Field name made lowercase.
    signaldate = models.DateTimeField(db_column='SignalDate', blank=True, null=True, db_comment='Дата уровня сигнала')  # Field name made lowercase.
    isreference = models.IntegerField(db_column='IsReference', blank=True, null=True, db_comment='Сделать прибор "эталонным": 1 ')  # Field name made lowercase.
    workmode = models.SmallIntegerField(db_column='WorkMode', blank=True, null=True, db_comment='Режим работы прибора: 0 - толь')  # Field name made lowercase.
    #currentchannel = models.ForeignKey(Channeltypes, models.DO_NOTHING, db_column='CurrentChannel_id', blank=True, null=True, db_comment='Channels.ChannelType_id')  # Field name made lowercase.
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
    #currentsim = models.ForeignKey('Sims', models.DO_NOTHING, db_column='CurrentSIM', blank=True, null=True, db_comment='Текущая Sim карта, на которой ')  # Field name made lowercase.
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
    
    def __str__(self):
        return f'{self.pult_name}'

class Serviceorganization(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    servicename = models.CharField(db_column='ServiceName', unique=True, max_length=500)  # Field name made lowercase.
    idcode = models.CharField(db_column='IDCode', max_length=50, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ServiceOrganization'

class Statusgroupresponse(models.Model):
    status_id = models.AutoField(primary_key=True, db_comment='ID')
    status = models.IntegerField(blank=True, null=True, db_comment='Дополнительный статус группы: ')
    reason = models.CharField(max_length=150, blank=True, null=True, db_comment='Описание')
    issystem = models.BooleanField(db_column='IsSystem', db_comment='Системное состояние: 1 - да; 0')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'StatusGroupResponse'
        db_table_comment = 'Состояния групп реагирования'
