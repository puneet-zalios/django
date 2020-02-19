from django.db import models

class Facility(models.Model):
    facilityid = models.CharField(primary_key=True, max_length=32)
    updateddate = models.DateTimeField()
    updatedby = models.CharField(max_length=128)
    createddate = models.DateTimeField()
    createdby = models.CharField(max_length=128)
    organizationid = models.CharField(max_length=32)
#    orgattr1 = models.CharField(max_length=128)
#    orgattr2 = models.CharField(max_length=128)
#    orgattr3 = models.CharField(max_length=128)
#    orgattr4 = models.CharField(max_length=128)
#    orgattr5 = models.CharField(max_length=128)
#    longitude = models.FloatField(max_digits=8, decimal_places=5)
    longitude = models.FloatField()
#    latitude = models.FloatField(max_digits=8, decimal_places=5)
    latitude = models.FloatField()
    street = models.CharField(max_length=511)
    city = models.CharField(max_length=127)
    county = models.CharField(max_length=127)
    district = models.CharField(max_length=511)
    stateprovince = models.CharField(max_length=63)
    region = models.CharField(max_length=127)
    country = models.CharField(max_length=255)
    facilityname = models.CharField(max_length=1027)
#    facilitystatus = models.CharField(max_length=127)
    facilitytype = models.CharField(max_length=127)
    currentstatus = models.IntegerField()
#    statusorder = models.IntegerField()
    
    class Meta:
        db_table = 'fusion.vw_facility'
        managed = False

    def __str__(self):
        return str(self.facilityname)

class Incidents(models.Model):
    incidentid = models.CharField(primary_key=True, max_length=32)
    updateddate = models.DateTimeField()
    updatedby = models.CharField(max_length=128)
    createddate = models.DateTimeField()
    createdby = models.CharField(max_length=128)
    incactivityid = models.DateTimeField()
    currentstatus = models.CharField(max_length=64)
    startdate = models.DateTimeField()
    enddate = models.DateTimeField()
    latestactivityid = models.DateTimeField()
    
    def __str__(self):
        return str(self.createddate)

    class Meta:
        db_table = 'fusion.tbl_incidents'
        managed = False

class IncActivity(models.Model):
    incidentid = models.CharField(max_length=32)
    incactivityid = models.DateTimeField(primary_key=True)
    updateddate = models.DateTimeField()
    updatedby = models.CharField(max_length=63)
    createddate = models.DateTimeField()
    createdby = models.CharField(max_length=63)
    incidentcategory = models.CharField(max_length=63)
    incidenttype = models.CharField(max_length=127)
    landmarkfacility = models.CharField(max_length=255)
    street = models.CharField(max_length=255)
    building = models.CharField(max_length=255)
    crossstreet = models.CharField(max_length=255)
    district = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    county = models.CharField(max_length=255)
    stateprovince = models.CharField(max_length=255)
    postal = models.CharField(max_length=127)
    region = models.CharField(max_length=255)
    country = models.CharField(max_length=255)
#    longitude = models.FloatField(max_digits=8, decimal_places=5)
    longitude = models.FloatField()
#    latitude = models.FloatField(max_digits=8, decimal_places=5)
    latitude = models.FloatField()
    approximate = models.BooleanField()
    activitystatus = models.CharField(max_length=63)
    severity = models.CharField(max_length=63)
    dateoccurred = models.DateTimeField()
    program = models.CharField(max_length=255)
    infosource = models.CharField(max_length=255)
    infoquality = models.CharField(max_length=255)
    gist = models.CharField(max_length=127)
    description = models.CharField(max_length=2047)
    channel = models.CharField(max_length=255)
    notifyrule = models.CharField(max_length=255)
    assignedunit = models.CharField(max_length=255)
    leadagency = models.CharField(max_length=255)
    updateflag = models.IntegerField()
    eteamflag = models.IntegerField()
    conversationlog = models.CharField(max_length=1023)
    attachmentlist = models.CharField(max_length=1023)
    commentflag = models.IntegerField()

    class Meta:
        db_table = 'fusion.tbl_incactivity'
        managed = False

class Attachments(models.Model):
    attachid = models.CharField(primary_key=True, max_length=32)
    createddate = models.DateTimeField()
    createdby = models.CharField(max_length=64)
    incidentid = models.CharField(max_length=32)
    incactivityid = models.DateTimeField()
    commentid = models.CharField(max_length=32)
    mimetype = models.CharField(max_length=32)
    attachdata = models.CharField(max_length=2047)
    linkdata = models.CharField(max_length=1023)
    label = models.CharField(max_length=1023)

    class Meta:
        db_table = 'fusion.tbl_incattachments'
        managed = False