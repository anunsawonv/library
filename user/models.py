# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class LmsAllbooks(models.Model):
    book_id = models.AutoField(primary_key=True)
    class_id = models.IntegerField()
    catid = models.IntegerField(db_column='catID')  # Field name made lowercase.
    book_title = models.CharField(max_length=255)
    callno = models.CharField(db_column='callNo', max_length=255)  # Field name made lowercase.
    author = models.CharField(max_length=255)
    datepublish = models.CharField(max_length=255)
    availability = models.CharField(max_length=255)
    dateadded = models.DateTimeField(db_column='dateAdded')  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'lms_allbooks'


class LmsBookcategory(models.Model):
    cat_id = models.AutoField(primary_key=True)
    bookcategory = models.CharField(db_column='bookCategory', max_length=255)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'lms_bookcategory'


class LmsBorrow(models.Model):
    brid = models.AutoField(db_column='BRID', primary_key=True)  # Field name made lowercase.
    lrn_no = models.CharField(max_length=255)
    book_id = models.IntegerField()
    status = models.CharField(max_length=255)
    datetrack = models.DateTimeField(db_column='dateTrack')  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'lms_borrow'


class LmsBorrowreturn(models.Model):
    brid = models.AutoField(db_column='BRID', primary_key=True)  # Field name made lowercase.
    lrn_no = models.IntegerField()
    book_id = models.IntegerField()
    status = models.CharField(max_length=255)
    returndateuntil = models.CharField(db_column='returnDateUntil', max_length=255)  # Field name made lowercase.
    dateborrow = models.CharField(db_column='dateBorrow', max_length=255)  # Field name made lowercase.
    datereturn = models.CharField(db_column='dateReturn', max_length=255)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'lms_borrowreturn'


class LmsCategory(models.Model):
    catid = models.AutoField(db_column='catID', primary_key=True)  # Field name made lowercase.
    category = models.CharField(db_column='Category', max_length=255)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'lms_category'


class LmsClassification(models.Model):
    class_id = models.AutoField(primary_key=True)
    bookclassification = models.CharField(db_column='bookClassification', max_length=255)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'lms_classification'


class LmsFinefees(models.Model):
    fine_id = models.AutoField(primary_key=True)
    category = models.CharField(max_length=255)
    penalty = models.CharField(max_length=255)

    class Meta:
        managed = True
        db_table = 'lms_finefees'


class LmsLogs(models.Model):
    logid = models.AutoField(db_column='LogID', primary_key=True)  # Field name made lowercase.
    lrn_no = models.IntegerField()
    book_id = models.IntegerField()
    status = models.CharField(max_length=255)
    datetrack = models.DateTimeField(db_column='dateTrack')  # Field name made lowercase.
    dateuntil = models.CharField(db_column='dateUntil', max_length=255)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'lms_logs'


class LmsNonstudent(models.Model):
    username = models.CharField(max_length=20, blank=True, null=True)
    name = models.CharField(max_length=20, blank=True, null=True)
    address = models.CharField(max_length=50, blank=True, null=True)
    contact = models.CharField(max_length=20, blank=True, null=True)
    dateregistered = models.DateField(blank=True, null=True)
    password = models.CharField(max_length=10, blank=True, null=True)
    status = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'lms_nonstudent'


class LmsReturn(models.Model):
    brid = models.IntegerField(db_column='BRID')  # Field name made lowercase.
    lrn_no = models.CharField(max_length=255)
    book_id = models.IntegerField()
    status = models.CharField(max_length=255)
    datereturn = models.DateTimeField(db_column='dateReturn')  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'lms_return'


class LmsStudentrecord(models.Model):
    lrn_no = models.CharField(unique=True, max_length=255)
    studentname = models.CharField(db_column='studentName', max_length=255)  # Field name made lowercase.
    grade = models.CharField(max_length=255)

    class Meta:
        managed = True
        db_table = 'lms_studentrecord'


class Logs(models.Model):
    logid = models.AutoField(db_column='LogID', primary_key=True)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=100)  # Field name made lowercase.
    role = models.CharField(db_column='Role', max_length=100)  # Field name made lowercase.
    marks = models.CharField(db_column='Marks', max_length=255, db_collation='utf8mb4_unicode_ci')  # Field name made lowercase.
    dateop = models.DateTimeField(db_column='DateOp')  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'logs'


class Student(models.Model):
    registerid = models.AutoField(db_column='RegisterID', primary_key=True)  # Field name made lowercase.
    refno = models.CharField(db_column='RefNo', max_length=255, blank=True, null=True)  # Field name made lowercase.
    qrcode = models.TextField(blank=True, null=True)
    lrn = models.CharField(db_column='LRN', max_length=255, blank=True, null=True)  # Field name made lowercase.
    lastname = models.CharField(db_column='LastName', max_length=255, blank=True, null=True)  # Field name made lowercase.
    firstname = models.CharField(db_column='FirstName', max_length=255, blank=True, null=True)  # Field name made lowercase.
    middlename = models.CharField(db_column='MiddleName', max_length=255, blank=True, null=True)  # Field name made lowercase.
    suffix = models.CharField(db_column='Suffix', max_length=255, blank=True, null=True)  # Field name made lowercase.
    gender = models.CharField(db_column='Gender', max_length=255, blank=True, null=True)  # Field name made lowercase.
    birthdate = models.CharField(db_column='BirthDate', max_length=255, blank=True, null=True)  # Field name made lowercase.
    birthplace = models.CharField(db_column='BirthPlace', max_length=255, blank=True, null=True)  # Field name made lowercase.
    address = models.CharField(db_column='Address', max_length=255, blank=True, null=True)  # Field name made lowercase.
    ethnicity = models.CharField(db_column='Ethnicity', max_length=255, blank=True, null=True)  # Field name made lowercase.
    religion = models.CharField(db_column='Religion', max_length=255, blank=True, null=True)  # Field name made lowercase.
    contact = models.CharField(db_column='Contact', max_length=255, blank=True, null=True)  # Field name made lowercase.
    email = models.CharField(db_column='Email', max_length=255, blank=True, null=True)  # Field name made lowercase.
    level = models.CharField(db_column='Level', max_length=255, blank=True, null=True)  # Field name made lowercase.
    strand = models.CharField(db_column='Strand', max_length=255, blank=True, null=True)  # Field name made lowercase.
    fathersname = models.CharField(db_column='FathersName', max_length=255, blank=True, null=True)  # Field name made lowercase.
    fathersoccupation = models.CharField(db_column='FathersOccupation', max_length=255, blank=True, null=True)  # Field name made lowercase.
    fatherscontact = models.CharField(db_column='FathersContact', max_length=255, blank=True, null=True)  # Field name made lowercase.
    mothersname = models.CharField(db_column='MothersName', max_length=255, blank=True, null=True)  # Field name made lowercase.
    mothersoccupation = models.CharField(db_column='MothersOccupation', max_length=255, blank=True, null=True)  # Field name made lowercase.
    motherscontact = models.CharField(db_column='MothersContact', max_length=255, blank=True, null=True)  # Field name made lowercase.
    guardiansname = models.CharField(db_column='GuardiansName', max_length=255, blank=True, null=True)  # Field name made lowercase.
    guardiansoccupation = models.CharField(db_column='GuardiansOccupation', max_length=255, blank=True, null=True)  # Field name made lowercase.
    guardianscontact = models.CharField(db_column='GuardiansContact', max_length=255, blank=True, null=True)  # Field name made lowercase.
    curriculum = models.CharField(db_column='Curriculum', max_length=255, blank=True, null=True)  # Field name made lowercase.
    civilstatus = models.CharField(db_column='CivilStatus', max_length=255, blank=True, null=True)  # Field name made lowercase.
    juniorhigh = models.CharField(db_column='JuniorHigh', max_length=255, blank=True, null=True)  # Field name made lowercase.
    seniorhigh = models.CharField(db_column='SeniorHigh', max_length=255, blank=True, null=True)  # Field name made lowercase.
    junioraddress = models.CharField(db_column='JuniorAddress', max_length=255, blank=True, null=True)  # Field name made lowercase.
    senioraddress = models.CharField(db_column='SeniorAddress', max_length=255, blank=True, null=True)  # Field name made lowercase.
    techvoccourse = models.CharField(db_column='TechvocCourse', max_length=255, blank=True, null=True)  # Field name made lowercase.
    culturalminoritygroup = models.CharField(db_column='CulturalMinorityGroup', max_length=255, blank=True, null=True)  # Field name made lowercase.
    disabilities = models.CharField(db_column='Disabilities', max_length=255, blank=True, null=True)  # Field name made lowercase.
    birthcert = models.CharField(db_column='BirthCert', max_length=255, blank=True, null=True)  # Field name made lowercase.
    form137 = models.CharField(db_column='Form137', max_length=255, blank=True, null=True)  # Field name made lowercase.
    goodmoral = models.CharField(db_column='GoodMoral', max_length=255, blank=True, null=True)  # Field name made lowercase.
    reportcard = models.CharField(db_column='ReportCard', max_length=255, blank=True, null=True)  # Field name made lowercase.
    esc = models.CharField(db_column='ESC', max_length=255, blank=True, null=True)  # Field name made lowercase.
    psa = models.CharField(db_column='PSA', max_length=255, blank=True, null=True)  # Field name made lowercase.
    number_2x2 = models.CharField(db_column='2x2', max_length=255, blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    dateregistered = models.CharField(db_column='DateRegistered', max_length=255, blank=True, null=True)  # Field name made lowercase.
    password = models.CharField(max_length=45, blank=True, null=True)
    status = models.CharField(max_length=45, blank=True, null=True)

    def __str__(self):
        return str(self.registerid)

    class Meta:
        managed = True
        db_table = 'student'


class Teachers(models.Model):
    teacherid = models.AutoField(db_column='teacherId', primary_key=True)  # Field name made lowercase.
    email = models.CharField(max_length=255, blank=True, null=True)
    password = models.CharField(max_length=255, blank=True, null=True)
    lastname = models.CharField(db_column='Lastname', max_length=255, blank=True, null=True)  # Field name made lowercase.
    firstname = models.CharField(db_column='Firstname', max_length=250, blank=True, null=True)  # Field name made lowercase.
    middlename = models.CharField(db_column='Middlename', max_length=255, blank=True, null=True)  # Field name made lowercase.
    suffix = models.CharField(db_column='Suffix', max_length=255)  # Field name made lowercase.
    age = models.IntegerField(db_column='Age', blank=True, null=True)  # Field name made lowercase.
    dateofbirth = models.CharField(db_column='DateOfBirth', max_length=255, blank=True, null=True)  # Field name made lowercase.
    placeofbirth = models.CharField(db_column='PlaceOfBirth', max_length=255, blank=True, null=True)  # Field name made lowercase.
    contactno = models.CharField(db_column='ContactNo', max_length=255, blank=True, null=True)  # Field name made lowercase.
    gender = models.CharField(db_column='Gender', max_length=255, blank=True, null=True)  # Field name made lowercase.
    maritalstatus = models.CharField(db_column='MaritalStatus', max_length=255, blank=True, null=True)  # Field name made lowercase.
    citizenship = models.CharField(db_column='Citizenship', max_length=255, blank=True, null=True)  # Field name made lowercase.
    religion = models.CharField(db_column='Religion', max_length=255, blank=True, null=True)  # Field name made lowercase.
    address = models.CharField(db_column='Address', max_length=255, blank=True, null=True)  # Field name made lowercase.
    homeaddress = models.CharField(db_column='HomeAddress', max_length=255)  # Field name made lowercase.
    gacademicyearid = models.IntegerField(db_column='GAcademicYearID')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'teachers'


class Users(models.Model):
    name = models.CharField(max_length=250, blank=True, null=True)
    username = models.CharField(unique=True, max_length=250, blank=True, null=True)
    password = models.CharField(max_length=250, blank=True, null=True)
    userrole = models.CharField(max_length=150, blank=True, null=True)
    macaddress = models.CharField(db_column='macAddress', max_length=250, blank=True, null=True)  # Field name made lowercase.
    status = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'users'