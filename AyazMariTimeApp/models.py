from datetime import datetime

from django.conf import settings
from django.contrib.auth.models import User
from django.db import models
from django.forms import ModelForm, forms
from django import forms

from django.utils import timezone
from django.utils.safestring import mark_safe
# Create your models here.
DATE_INPUT_FORMATS = ('%d/%m/%Y','%d-%m-%Y','%Y-%m-%d')


ACTIVE_CHOICES = (
    ('1', 'Active'),
    ('0', 'In Active')
)
ONBOARD_CHOICES = (
    ('1', 'YES'),
    ('2', 'NO'),
    ('3', 'GAP')
)



class VTMaster(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100)
    status = models.CharField(choices=ACTIVE_CHOICES, max_length=10, default='1')

    def __str__(self):
        return self.title

class VSMaster(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100)
    status = models.CharField(choices=ACTIVE_CHOICES, max_length=10, default='1')

    def __str__(self):
        return self.title

class FLAGMaster(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100)
    status = models.CharField(choices=ACTIVE_CHOICES, max_length=10, default='1')

    def __str__(self):
        return self.title

class CURRENCYMaster(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100)
    status = models.CharField(choices=ACTIVE_CHOICES, max_length=10, default='1')

    def __str__(self):
        return self.title

class SHIP2Master(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100)
    status = models.CharField(choices=ACTIVE_CHOICES, max_length=10, default='1')

    def __str__(self):
        return self.title

class PUMPMaster(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100)
    status = models.CharField(choices=ACTIVE_CHOICES, max_length=10, default='1')

    def __str__(self):
        return self.title

class ENGMaster(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100)
    status = models.CharField(choices=ACTIVE_CHOICES, max_length=10, default='1')

    def __str__(self):
        return self.title

class VISAMaster(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100)
    status = models.CharField(choices=ACTIVE_CHOICES, max_length=10, default='1')

    def __str__(self):
        return self.title

class GAPMaster(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100)
    status = models.CharField(choices=ACTIVE_CHOICES, max_length=10, default='1')

    def __str__(self):
        return self.title

class SCMaster(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100)
    status = models.CharField(choices=ACTIVE_CHOICES, max_length=10, default='1')

    def __str__(self):
        return self.title

class PAYMaster(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100)
    status = models.CharField(choices=ACTIVE_CHOICES, max_length=10, default='1')

    def __str__(self):
        return self.title

class RANKMaster(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100)
    status = models.CharField(choices=ACTIVE_CHOICES, max_length=10, default='1')
    orderid = models.IntegerField(max_length=3,verbose_name='Ordering ID',unique=True)

    class Meta:
        ordering = ['orderid']

    def __str__(self):
        return self.title



class DumpData(models.Model):
    id = models.AutoField(primary_key=True,verbose_name='ID2')
    name = models.CharField(max_length=50,blank=True,verbose_name='NAME')
    vt = models.ForeignKey(VTMaster, on_delete=models.CASCADE, null=True,verbose_name='VT',blank=False,default=17)
    vs = models.ForeignKey(VSMaster, on_delete=models.CASCADE, null=True,verbose_name='VS',blank=False,default=6)
    rank = models.ForeignKey(RANKMaster, on_delete=models.CASCADE, null=True,verbose_name='RANK',blank=False,related_name='dumpdata_set',default=35)
    rank2 =models.ForeignKey(RANKMaster, on_delete=models.CASCADE, null=True,verbose_name='RANK2',blank=False,related_name='dumpdata_set2',default=35)
    mobno=models.CharField(max_length=20,blank=True,verbose_name='MOBILE NO',unique=True,default='',null=True)
    emailid=models.CharField(max_length=50,blank=True,verbose_name='EMAIL ID',default='',null=True)


    flag = models.ForeignKey(FLAGMaster, on_delete=models.CASCADE, null=True,verbose_name='FLAG',blank=False,default=32)
    customid=models.CharField(max_length=50,blank=True,verbose_name='ID',unique=True,null=True)

    pay1=models.BigIntegerField(max_length=10,blank=True,verbose_name='PAY 1')
    pay2=models.BigIntegerField(max_length=10,blank=True,verbose_name='PAY 2')
    currency = models.ForeignKey(CURRENCYMaster, on_delete=models.CASCADE, null=True,verbose_name='CURRENCY',blank=True,default=7)

    alvdate=models.DateField(blank=True,verbose_name='AVL DATE',default='',null=True)
    onb = models.CharField(choices=ONBOARD_CHOICES,max_length=10,blank=True,verbose_name='ONB')
    ship2 = models.ForeignKey(SHIP2Master, on_delete=models.CASCADE, null=True,verbose_name='SHIP2',blank=False,default=16)
    pump = models.ForeignKey(PUMPMaster, on_delete=models.CASCADE, null=True,verbose_name='PUMP',blank=False,default=4)
    pump = models.ForeignKey(PUMPMaster, on_delete=models.CASCADE, null=True,verbose_name='PUMP',blank=False,default=4)
    eng = models.ForeignKey(ENGMaster, on_delete=models.CASCADE, null=True,verbose_name='ENG',blank=False,default=4)
    dob=models.DateField(blank=True,verbose_name='DATE OF BIRTH',null=True)


    cdc = models.CharField(max_length=50,blank=True,verbose_name='CDC')
    passport = models.CharField(max_length=50,blank=True,verbose_name='PASSPORT',unique=True,default='',null=True)
    visa = models.ForeignKey(VISAMaster, on_delete=models.CASCADE, null=True,verbose_name='VISA',blank=False,default=8)
    agn = models.CharField(max_length=50,blank=True,verbose_name='AGN')
    # gap = models.ForeignKey(GAPMaster, on_delete=models.CASCADE, null=True,verbose_name='GAP',blank=False)
    sc = models.ForeignKey(SCMaster, on_delete=models.CASCADE, null=True,verbose_name='SC',blank=False,default=3)
    pay = models.ForeignKey(PAYMaster, on_delete=models.CASCADE, null=True,verbose_name='PAY',blank=False,default=6)
    cno = models.CharField(max_length=50,blank=True,verbose_name='CNO')
    comp = models.CharField(max_length=50,blank=True,verbose_name='COMP')

    vf = models.CharField(max_length=100,blank=True,verbose_name='VF')
    vn = models.CharField(max_length=100,blank=True,verbose_name='VN')
    doc = models.DateField(blank=True,verbose_name='DOC',default='',null=True)
    so = models.DateField(blank=True,verbose_name='SO',default='',null=True)
    sof = models.DateField(blank=True,verbose_name='SOF',default='',null=True)
    doc1 = models.DateField(blank=True,verbose_name='DOC1',default='',null=True)


    remarks = models.CharField(max_length=500,blank=True,verbose_name='REMARKS')
    createdate = models.DateTimeField(auto_now_add=True,null=True,blank=True)
    updatedate = models.DateTimeField(auto_now_add=True,null=True,blank=True)

    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)
    #     self.updatedate = self.active

    def save(self, *args, **kwargs):
        #if self.is_active and not self.__is_active:
        self.updatedate = datetime.now()

        if self.name!=None:
             self.name = self.name.upper()

        if self.customid!=None:
            self.customid = self.customid.upper()

        if self.cdc!=None:
             self.cdc = self.cdc.upper()

        if self.emailid!=None:
             self.emailid = self.emailid.upper()

        if self.passport!=None:
            self.passport = self.passport.upper()

        if self.agn!=None:
            self.agn = self.agn.upper()

        if self.cno!=None:
             self.cno = self.cno.upper()

        if self.comp!=None:
             self.comp = self.comp.upper()

        if self.vf!=None:
             self.vf = self.vf.upper()

        if self.vn!=None:
            self.vn = self.vn.upper()



        if self.remarks != None:
            self.remarks = self.remarks.upper()


        # if not self.pk:
        #     # This is a new object, so record the creator
        #     self.created_by = request.user
        # else:
        #     # This is an existing object, so record the editor
        #     self.modified_by = request.user


        super().save(*args, **kwargs)


    # createdat=models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.name


