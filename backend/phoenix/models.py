from django.db import models

class Advancesearchtemplates(models.Model):
    #id = models.PositiveIntegerField()
    typeoptions = models.SmallIntegerField(db_column='TypeOptions', blank=True, null=True)  # Field name made lowercase.
    templatename = models.CharField(db_column='TemplateName', max_length=200)  # Field name made lowercase.
    sqlstring = models.CharField(db_column='SQLString', max_length=5000)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'AdvanceSearchTemplates'

    def __str__(self):
        return f'{self.id}-{self.typeoptions}-{self.templatename}'
    
class Areas(models.Model):
    area_id = models.AutoField(db_column='Area_id', primary_key=True, db_comment='ID')  # Field name made lowercase.
    area_name = models.CharField(db_column='Area_name', unique=True, max_length=200, blank=True, null=True, db_comment='Название района')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Areas'
        db_table_comment = 'Районы'

    def __str__(self):
        return f'{self.area_name}'

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
        return f'{self.company_id}-{self.companyname}-{self.address}    '
    
class Customers(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    organization = models.CharField(db_column='Organization', max_length=500, blank=True, null=True)  # Field name made lowercase.
    organizationaddress = models.CharField(db_column='OrganizationAddress', max_length=500, blank=True, null=True)  # Field name made lowercase.
    director = models.CharField(db_column='Director', max_length=500, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Customers'

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
