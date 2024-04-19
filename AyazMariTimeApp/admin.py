from django.contrib import admin
from django.contrib.admin import AdminSite, sites

# // ./manage.py makemigrations AyazMariTimeApp
from AyazMariTimeApp.models import DumpData,VTMaster,VSMaster,FLAGMaster,CURRENCYMaster,SHIP2Master,PUMPMaster,ENGMaster,VISAMaster
from AyazMariTimeApp.models import GAPMaster,SCMaster,PAYMaster,RANKMaster
from django_admin_listfilter_dropdown.filters import DropdownFilter, RelatedDropdownFilter, ChoiceDropdownFilter

# admin.site.register(DumpData)
# admin.site.register(VTMaster)
# admin.site.register(VSMaster)
# admin.site.register(FLAGMaster)
# admin.site.register(CURRENCYMaster)
# admin.site.register(SHIP2Master)
# admin.site.register(PUMPMaster)
# admin.site.register(ENGMaster)



# class EventAdminSite(AdminSite):
#     def get_app_list(self,request,app_label=None):
#         ordering={
#             'Dump datas':1,
#             'Rank masters':2,
#             'Pay masters':3,
#             'Sc masters':4,
#             'Gap masters':5,
#             'Visa masters':6,
#             'Eng masters':7,
#             'Pump masters':8,
#             'Shi p2 masters':9,
#             'Currency masters':10,
#             'Flag masters':11,
#             'Vt masters':12,
#             'Vs masters':13,
#             # 'Manage Role':14,
#             # 'Manage Tier Type':15,
#             # 'Manage Lifecycle Stage':16,
#         }
#         app_dict=self._build_app_dict(request,app_label)
#         app_list=sorted(app_dict.values(),key=lambda x:x['name'].lower())
#         for app in app_list:
#             app['models'].sort(key=lambda x:ordering[x['name']])
#         return app_list
# mysite=EventAdminSite()
# admin.site=mysite
# sites.site=mysite


@admin.register(DumpData)
class DumpDataAdmin(admin.ModelAdmin):
    model = DumpData
    list_display = ('id', 'name','vt','vs','rank','rank2','flag','customid',
                    'pay1','currency','pay2','alvdate','onb','ship2','mobno','pump',
                    'eng','dob','cdc','passport','visa','agn','sc','pay','cno','comp','remarks')
    list_filter = ['vt', 'vs','rank','rank2','flag','onb','flag','ship2','pump','eng','currency','onb','visa','sc']
    # list_filter = (
    #     # for ordinary fields
    #     ('vt', RelatedDropdownFilter),
    #     # for choice fields
    #     ('vs', RelatedDropdownFilter),
    #     # for related fields
    #     ('rank', RelatedDropdownFilter),
    #     ('rank2', RelatedDropdownFilter),
    #     ('flag', RelatedDropdownFilter),
    #     ('ship2', RelatedDropdownFilter),
    #     ('pump', RelatedDropdownFilter),
    #     ('eng', RelatedDropdownFilter),
    #     ('pay', RelatedDropdownFilter),
    #     ('currency', RelatedDropdownFilter),
    #     ('onb', ChoiceDropdownFilter),
    #
    #     ('visa', RelatedDropdownFilter),
    #     ('sc', RelatedDropdownFilter),
    #
    # )


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
    list_filter = ['status']

@admin.register(PAYMaster)
class PAYMasterAdmin(admin.ModelAdmin):
    model = PAYMaster
    list_display = ('id', 'title','status')


@admin.register(RANKMaster)
class RANKMasterAdmin(admin.ModelAdmin):
    model = RANKMaster
    list_display = ('id', 'title','status')
    # ordering = ['title']