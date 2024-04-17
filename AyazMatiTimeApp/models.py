from django.contrib.auth.models import User
from django.db import models
from django.forms import ModelForm
from django.utils import timezone
from django.utils.safestring import mark_safe
# Create your models here.

ACTIVE_CHOICES = (
    ('1', 'Active'),
    ('0', 'In Active')
)
ONB_CHOICES = (
    ('1', 'YES'),
    ('0', 'NO')
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



class DumpData(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50,blank=False,verbose_name='NAME')
    vt = models.ForeignKey(VTMaster, on_delete=models.CASCADE, null=True,verbose_name='VT',blank=False)
    vs = models.ForeignKey(VSMaster, on_delete=models.CASCADE, null=True,verbose_name='VS',blank=False)
    rank = models.CharField(max_length=50,blank=True,verbose_name='RANK')
    rank2 = models.CharField(max_length=50,blank=True,verbose_name='RANK2')
    flag = models.ForeignKey(FLAGMaster, on_delete=models.CASCADE, null=True,verbose_name='FLAG',blank=False)
    customid=models.IntegerField(max_length=10,blank=False,verbose_name='ID')
    customid2=models.IntegerField(max_length=10,blank=False,verbose_name='ID2')
    pay1=models.IntegerField(max_length=10,blank=False,verbose_name='PAY 1')
    currency = models.ForeignKey(CURRENCYMaster, on_delete=models.CASCADE, null=True,verbose_name='CURRENCY',blank=False)
    exppay=models.IntegerField(max_length=10,blank=False,verbose_name='EXP PAY')
    alvdate=models.DateField(blank=False,verbose_name='AVL DATE',default=timezone.now)
    onb = models.CharField(max_length=50,blank=True,verbose_name='ONB')
    ship2 = models.ForeignKey(SHIP2Master, on_delete=models.CASCADE, null=True,verbose_name='SHIP2',blank=False)
    mobno=models.BigIntegerField(max_length=15,blank=False,verbose_name='MOBILE NO')
    pump = models.ForeignKey(PUMPMaster, on_delete=models.CASCADE, null=True,verbose_name='PUMP',blank=False)
    eng = models.ForeignKey(ENGMaster, on_delete=models.CASCADE, null=True,verbose_name='ENG',blank=False)
    dob=models.DateField(blank=False,verbose_name='DATE OF BIRTH')
    cdc = models.CharField(max_length=50,blank=True,verbose_name='CDC')
    passport = models.CharField(max_length=50,blank=True,verbose_name='PASSPORT',unique=True)
    visa = models.ForeignKey(VISAMaster, on_delete=models.CASCADE, null=True,verbose_name='VISA',blank=False)
    agn = models.CharField(max_length=50,blank=True,verbose_name='AGN')
    gap = models.ForeignKey(GAPMaster, on_delete=models.CASCADE, null=True,verbose_name='GAP',blank=False)
    sc = models.ForeignKey(SCMaster, on_delete=models.CASCADE, null=True,verbose_name='SC',blank=False)
    pay = models.ForeignKey(PAYMaster, on_delete=models.CASCADE, null=True,verbose_name='PAY',blank=False)
    cno = models.CharField(max_length=50,blank=True,verbose_name='CNO')
    comp = models.CharField(max_length=50,blank=True,verbose_name='COMP')
    remarks = models.CharField(max_length=50,blank=True,verbose_name='REMARKS')
    # createdat=models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.name