from django.contrib import admin
# // ./manage.py makemigrations AyazMatiTimeApp
from AyazMatiTimeApp.models import DumpData,VTMaster,VSMaster,FLAGMaster,CURRENCYMaster,SHIP2Master,PUMPMaster,ENGMaster,VISAMaster
from AyazMatiTimeApp.models import GAPMaster,SCMaster,PAYMaster

# admin.site.register(DumpData)
# admin.site.register(VTMaster)
# admin.site.register(VSMaster)
# admin.site.register(FLAGMaster)
# admin.site.register(CURRENCYMaster)
# admin.site.register(SHIP2Master)
# admin.site.register(PUMPMaster)
# admin.site.register(ENGMaster)

@admin.register(DumpData)
class DumpDataAdmin(admin.ModelAdmin):
    model = DumpData
    list_display = ('id', 'name','vt','vs','rank','rank2','flag','customid','customid2',
                    'pay1','currency','exppay','alvdate','onb','ship2','mobno','pump',
                    'eng','dob','cdc','passport','visa','agn','gap','sc','pay','cno','comp','remarks')
    # list_filter = ['vt', 'vs']


@admin.register(VISAMaster)
class VISAMasterAdmin(admin.ModelAdmin):
    model = VISAMaster
    list_display = ('id', 'title','status')

@admin.register(VTMaster)
class VTMasterAdmin(admin.ModelAdmin):
    model = VTMaster
    list_display = ('id', 'title','status')

@admin.register(VSMaster)
class VSMasterAdmin(admin.ModelAdmin):
    model = VSMaster
    list_display = ('id', 'title','status')

@admin.register(FLAGMaster)
class FLAGMasterAdmin(admin.ModelAdmin):
    model = FLAGMaster
    list_display = ('id', 'title','status')

@admin.register(CURRENCYMaster)
class CURRENCYMasterAdmin(admin.ModelAdmin):
    model = CURRENCYMaster
    list_display = ('id', 'title','status')

@admin.register(SHIP2Master)
class SHIP2MasterAdmin(admin.ModelAdmin):
    model = SHIP2Master
    list_display = ('id', 'title','status')

@admin.register(PUMPMaster)
class PUMPMasterAdmin(admin.ModelAdmin):
    model = PUMPMaster
    list_display = ('id', 'title','status')

@admin.register(ENGMaster)
class ENGMasterAdmin(admin.ModelAdmin):
    model = ENGMaster
    list_display = ('id', 'title','status')

@admin.register(GAPMaster)
class GAPMasterAdmin(admin.ModelAdmin):
    model = GAPMaster
    list_display = ('id', 'title','status')

@admin.register(SCMaster)
class SCMasterAdmin(admin.ModelAdmin):
    model = SCMaster
    list_display = ('id', 'title','status')

@admin.register(PAYMaster)
class PAYMasterAdmin(admin.ModelAdmin):
    model = PAYMaster
    list_display = ('id', 'title','status')