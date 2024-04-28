# name,customid,pay1,pay2,alvdate,onb,mobno,dob,cdc,passport,agn,cno,comp,remarks,currency_id,eng_id,flag_id,pay_id,pump_id,sc_id,ship2_id,visa_id,vs_id,vt_id,rank_id,rank2_id
import csv
from io import StringIO

from django.contrib import admin
from django.contrib.admin import AdminSite, sites
from django.contrib import admin
from django.forms import models
from django.http import HttpResponse
from rangefilter.filters import DateRangeFilter

# // ./manage.py makemigrations AyazMariTimeApp
from AyazMariTimeApp.models import DumpData, VTMaster, VSMaster, FLAGMaster, CURRENCYMaster, SHIP2Master, PUMPMaster, \
    ENGMaster, VISAMaster
from AyazMariTimeApp.models import GAPMaster, SCMaster, PAYMaster, RANKMaster
from django_admin_listfilter_dropdown.filters import DropdownFilter, RelatedDropdownFilter, ChoiceDropdownFilter
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User
from import_export.admin import ExportActionMixin
from django import forms  # Add this import

from AyazMariTimeApp.resource import DumpDataResource

# admin.site.register(DumpData)
# admin.site.register(VTMaster)
# admin.site.register(VSMaster)
# admin.site.register(FLAGMaster)
# admin.site.register(CURRENCYMaster)
# admin.site.register(SHIP2Master)
# admin.site.register(PUMPMaster)
# admin.site.register(ENGMaster)



# class EventAdminSite(AdminSite):
#     def get_app_list(self, request, app_label=None):
#         ordering = {
#             'Dump datas': 1,
#             'Rank masters': 2,
#             'Pay masters': 3,
#             'Sc masters': 4,
#             'Gap masters': 5,
#             'Visa masters': 6,
#             'Eng masters': 7,
#             'Pump masters': 8,
#             'Shi p2 masters': 9,
#             'Currency masters': 10,
#             'Flag masters': 11,
#             'Vt masters': 12,
#             'Vs masters': 13,
#             # 'Manage Role': 14,
#             # 'Manage Tier Type': 15,
#             # 'Manage Lifecycle Stage': 16,
#         }
#         app_dict = self._build_app_dict(request, app_label)
#         app_list = sorted(app_dict.values(), key=lambda x: x['name'].lower())
#         for app in app_list:
#             app['models'].sort(key=lambda x: ordering.get(x['name'], float('inf')))
#         return app_list
#
# mysite = EventAdminSite()
# admin.site = mysite
# # Reset sites.site to default AdminSite instance to show user and group options
# sites.site = AdminSite()


# class EventAdminSite(AdminSite):
#     def get_app_list(self, request, app_label=None):
#         ordering = {
#             'Dump datas': 1,
#             'Rank masters': 2,
#             'Pay masters': 3,
#             'Sc masters': 4,
#             'Gap masters': 5,
#             'Visa masters': 6,
#             'Eng masters': 7,
#             'Pump masters': 8,
#             'Shi p2 masters': 9,
#             'Currency masters': 10,
#             'Flag masters': 11,
#             'Vt masters': 12,
#             'Vs masters': 13,
#             # 'Manage Role':14,
#             # 'Manage Tier Type':15,
#             # 'Manage Lifecycle Stage':16,
#         }
#         app_dict = self._build_app_dict(request, app_label)
#         app_list = sorted(app_dict.values(), key=lambda x: x['name'].lower())
#         for app in app_list:
#             app['models'].sort(key=lambda x: ordering[x['name']])
#         return app_list
#
#
# mysite = EventAdminSite()
# admin.site = mysite
# sites.site = mysite

class CustomUserAdmin(BaseUserAdmin):
    list_display = ('username', 'first_name','last_name','last_login_with_time')
    site_url = None

    def last_login_with_time(self, obj):
        return obj.last_login.strftime("%d-%m-%Y %H:%M:%S")

    last_login_with_time.short_description = 'Last Login Time'
    list_filter = []
    search_fields = []


# Re-register UserAdmin
admin.site.unregister(User)
admin.site.register(User, CustomUserAdmin)

# automatic autodiscover should be turned off in settings


from import_export.admin import ImportExportModelAdmin



# @admin.register(DumpData)
class DumpDataAdmin(ImportExportModelAdmin):
    resource_class = DumpDataResource

    actions_on_top = False
    actions_on_bottom = False
    date_hierarchy = 'alvdate'
    model = DumpData
    list_per_page = 100
    list_display = ('id', 'name', 'vt', 'vs', 'rank', 'rank2', 'flag', 'customid',
                    'pay1', 'currency', 'pay2', 'alvdate', 'onb', 'ship2', 'mobno', 'pump',
                    'eng', 'dob', 'cdc', 'passport', 'visa', 'agn', 'sc', 'pay', 'cno', 'comp')
    list_filter = ['vt', 'vs', 'rank', 'rank2', 'flag', 'onb', 'flag', 'ship2', 'pump', 'eng', 'currency',
                   'visa', 'sc', 'pay', 'alvdate']
    search_fields = ('name', 'mobno', 'customid', 'passport', 'remarks')
    # formfield_overrides = {
    #     models.TextField: {'remarks': forms.Textarea(attrs={'rows': 4, 'cols': 40})},
    # }

    def generate_sample_csv(self, request, queryset):
        # Generate sample CSV content
        output = StringIO()
        writer = csv.writer(output)
        writer.writerow([
            'id', 'name', 'vt', 'vs', 'rank', 'rank2', 'flag', 'customid',
            'pay1', 'currency', 'pay2', 'alvdate', 'onb', 'ship2', 'mobno', 'pump',
            'eng', 'dob', 'cdc', 'passport', 'visa', 'agn', 'sc', 'pay', 'cno', 'comp'
        ])
        writer.writerow([
            '1', 'John Doe', 'Merchant Navy', 'Officer', '1', '2', 'USA', '12345',
            '5000', 'USD', '6000', '2024-04-22', 'True', 'Vessel1', '123456789', 'Engineer',
            '1980-01-01', '123456', 'ABC12345', '1234567890123456', 'USA', '123456789', 'Senior',
            '6000', '123', 'Company1'
        ])
        writer.writerow([
            '2', 'Jane Smith', 'Merchant Navy', 'Officer', '2', '3', 'UK', '54321',
            '6000', 'GBP', '7000', '2024-04-23', 'True', 'Vessel2', '987654321', 'Deck Officer',
            '1975-05-05', '654321', 'BBC54321', '6543210987654321', 'UK', '987654321', 'Junior',
            '7000', '321', 'Company2'
        ])
        # You can add more sample rows if needed

        # Serve the sample CSV file as a downloadable response
        response = HttpResponse(output.getvalue(), content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename=sample_data.csv'
        return response
    generate_sample_csv.short_description = "Download Sample CSV"

    # Register the custom action
    actions = ['generate_sample_csv']

    def has_export_permission(self, request):
        if request.user.is_superuser:
            return True
        return False

    def has_import_permission(self, request):
        # if request.user.is_superuser:
        #     return True
        return False


admin.site.register(DumpData, DumpDataAdmin)


@admin.register(VISAMaster)
class VISAMasterAdmin(admin.ModelAdmin):
    model = VISAMaster
    list_display = ('id', 'title', 'status')


@admin.register(VTMaster)
class VTMasterAdmin(admin.ModelAdmin):
    model = VTMaster
    list_display = ('id', 'title', 'status')


@admin.register(VSMaster)
class VSMasterAdmin(admin.ModelAdmin):
    model = VSMaster
    list_display = ('id', 'title', 'status')


@admin.register(FLAGMaster)
class FLAGMasterAdmin(admin.ModelAdmin):
    model = FLAGMaster
    list_display = ('id', 'title', 'status')


@admin.register(CURRENCYMaster)
class CURRENCYMasterAdmin(admin.ModelAdmin):
    model = CURRENCYMaster
    list_display = ('id', 'title', 'status')


@admin.register(SHIP2Master)
class SHIP2MasterAdmin(admin.ModelAdmin):
    model = SHIP2Master
    list_display = ('id', 'title', 'status')


@admin.register(PUMPMaster)
class PUMPMasterAdmin(admin.ModelAdmin):
    model = PUMPMaster
    list_display = ('id', 'title', 'status')


@admin.register(ENGMaster)
class ENGMasterAdmin(admin.ModelAdmin):
    model = ENGMaster
    list_display = ('id', 'title', 'status')


@admin.register(GAPMaster)
class GAPMasterAdmin(admin.ModelAdmin):
    model = GAPMaster
    list_display = ('id', 'title', 'status')


@admin.register(SCMaster)
class SCMasterAdmin(admin.ModelAdmin):
    model = SCMaster
    list_display = ('id', 'title', 'status')
    list_filter = ['status']


@admin.register(PAYMaster)
class PAYMasterAdmin(admin.ModelAdmin):
    model = PAYMaster
    list_display = ('id', 'title', 'status')


@admin.register(RANKMaster)
class RANKMasterAdmin(admin.ModelAdmin):
    model = RANKMaster
    list_display = ('id', 'title', 'status')
    # ordering = ['title']
