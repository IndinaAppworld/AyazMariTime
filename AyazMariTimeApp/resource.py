from import_export import resources, fields
from import_export.widgets import ForeignKeyWidget

from .models import DumpData, VTMaster


class DumpDataResource(resources.ModelResource):
    # name = fields.Field(column_name='Name')

    ONBOARD_CHOICES = {
        '1': 'YES',
        '2': 'NO',
        '3': 'GAP',
    }

    foreign_key_name_VT = fields.Field(column_name='VT')
    foreign_key_name_VS = fields.Field(column_name='VS')
    foreign_key_name_RANK = fields.Field(column_name='RANK')
    foreign_key_name_RANK2 = fields.Field(column_name='RANK2')
    foreign_key_name_FLAG = fields.Field(column_name='FLAG')
    foreign_key_name_CURRENCY = fields.Field(column_name='CURRENCY')
    foreign_key_name_ONBOARD = fields.Field(column_name='ONBOARD')
    foreign_key_name_SHIP2 = fields.Field(column_name='SHIP2')
    foreign_key_name_PUMP = fields.Field(column_name='PUMP')
    foreign_key_name_ENG = fields.Field(column_name='ENG')
    foreign_key_name_VISA = fields.Field(column_name='VISA')
    foreign_key_name_SC = fields.Field(column_name='SC')
    foreign_key_name_PAY = fields.Field(column_name='PAY')
    custom_key_name_NAME = fields.Field(column_name='NAME')
    custom_key_name_MOBILENO = fields.Field(column_name='MOBILE NUMBER')
    custom_key_name_ID = fields.Field(column_name='ID')
    custom_key_name_PAY1 = fields.Field(column_name='PAY1')
    custom_key_name_PAY2 = fields.Field(column_name='PAY2')
    custom_key_name_AVAIBILITYDATE = fields.Field(column_name='AVAILABILTY DATE')
    custom_key_name_DATEOFBIRTH = fields.Field(column_name='DATE OF BIRTH')
    custom_key_name_CDC = fields.Field(column_name='CDC')
    custom_key_name_PASSPORT = fields.Field(column_name='PASSPORT')
    custom_key_name_AGN = fields.Field(column_name='AGN')
    custom_key_name_CNO = fields.Field(column_name='CNO')
    custom_key_name_COMP = fields.Field(column_name='COMP')
    custom_key_name_REMARKS = fields.Field(column_name='REMARKS')
    custom_key_name_ID2 = fields.Field(column_name='ID2')

    custom_key_name_VF = fields.Field(column_name='VF')
    custom_key_name_VN = fields.Field(column_name='VN')
    custom_key_name_DOC = fields.Field(column_name='DOC')
    custom_key_name_SO = fields.Field(column_name='SO')
    custom_key_name_SOF = fields.Field(column_name='SOF')
    custom_key_name_DOC1 = fields.Field(column_name='DOC1')
    custom_key_name_UPDATEDDATE = fields.Field(column_name='LAST UPDATE DATE')
    custom_key_name_EMAILID = fields.Field(column_name='EMAIL ID')

    class Meta:
        model = DumpData
        fields = ('custom_key_name_ID2', 'custom_key_name_NAME','custom_key_name_UPDATEDDATE', 'mobno','custom_key_name_EMAILID', 'foreign_key_name_VT', 'foreign_key_name_VS',
                  'foreign_key_name_RANK', 'foreign_key_name_RANK2',
                  'foreign_key_name_FLAG', 'customid', 'pay1', 'pay2', 'foreign_key_name_CURRENCY', 'alvdate',
                  'foreign_key_name_ONBOARD',
                  'foreign_key_name_SHIP2', 'foreign_key_name_PUMP', 'foreign_key_name_ENG',
                  'dob', 'cdc', 'passport', 'foreign_key_name_VISA',
                  'custom_key_name_VF','custom_key_name_VN','custom_key_name_DOC','custom_key_name_SO','custom_key_name_SOF','custom_key_name_DOC1'
                  'agn', 'foreign_key_name_SC',
                  'foreign_key_name_PAY', 'cno', 'comp', 'remarks')

        export_order = (
            'custom_key_name_ID2', 'custom_key_name_NAME', 'custom_key_name_UPDATEDDATE','custom_key_name_MOBILENO', 'custom_key_name_EMAILID','foreign_key_name_VT',
            'foreign_key_name_VS', 'foreign_key_name_RANK', 'foreign_key_name_RANK2',
            'foreign_key_name_FLAG', 'custom_key_name_ID', 'custom_key_name_PAY1', 'custom_key_name_PAY2',
            'foreign_key_name_CURRENCY', 'custom_key_name_AVAIBILITYDATE', 'foreign_key_name_ONBOARD',
            'foreign_key_name_SHIP2', 'foreign_key_name_PUMP', 'foreign_key_name_ENG',
            'custom_key_name_DATEOFBIRTH', 'custom_key_name_CDC', 'custom_key_name_PASSPORT', 'foreign_key_name_VISA',
            'custom_key_name_VF', 'custom_key_name_VN', 'custom_key_name_DOC', 'custom_key_name_SO',
            'custom_key_name_SOF', 'custom_key_name_DOC1','custom_key_name_AGN', 'foreign_key_name_SC', 'foreign_key_name_PAY', 'custom_key_name_CNO',
            'custom_key_name_COMP', 'custom_key_name_REMARKS')  # Specify the export order

        exclude = (
            'id', 'name', 'vt', 'vs', 'rank', 'rank2', 'mobno','emailid', 'flag', 'customid', 'pay1', 'pay2', 'currency',
            'alvdate',
            'onb', 'ship2', 'pump', 'eng', 'dob', 'cdc', 'passport', 'visa','vc','vf','doc','so','sof','doc1', 'agn', 'sc', 'pay', 'cno', 'comp',
            'remarks')

    def dehydrate_foreign_key_name_VT(self, obj):
        return obj.vt.title

    def dehydrate_foreign_key_name_VS(self, obj):
        return obj.vs.title

    def dehydrate_foreign_key_name_RANK(self, obj):
        return obj.rank.title

    def dehydrate_foreign_key_name_RANK2(self, obj):
        return obj.rank.title

    def dehydrate_foreign_key_name_CURRENCY(self, obj):
        return obj.currency.title

    def dehydrate_foreign_key_name_FLAG(self, obj):
        return obj.flag.title

    def dehydrate_foreign_key_name_ONBOARD(self, obj):
        flag_value = getattr(obj, 'onb')
        return self.ONBOARD_CHOICES.get(flag_value, flag_value)

    def dehydrate_foreign_key_name_SHIP2(self, obj):
        return obj.ship2.title

    def dehydrate_foreign_key_name_PUMP(self, obj):
        return obj.pump.title

    def dehydrate_foreign_key_name_ENG(self, obj):
        return obj.eng.title

    def dehydrate_foreign_key_name_SC(self, obj):
        return obj.sc.title

    def dehydrate_foreign_key_name_VISA(self, obj):
        return obj.visa.title

    def dehydrate_foreign_key_name_PAY(self, obj):
        return obj.pay.title

    def dehydrate_custom_key_name_NAME(self, obj):
        return obj.name

    def dehydrate_custom_key_name_MOBILENO(self, obj):
        return obj.mobno

    def dehydrate_custom_key_name_ID(self, obj):
        return obj.customid

    def dehydrate_custom_key_name_PAY1(self, obj):
        return obj.pay1

    def dehydrate_custom_key_name_PAY2(self, obj):
        return obj.pay2

    def dehydrate_custom_key_name_AVAIBILITYDATE(self, obj):
        return obj.alvdate

    def dehydrate_custom_key_name_DATEOFBIRTH(self, obj):
        return obj.alvdate

    def dehydrate_custom_key_name_CDC(self, obj):
        return obj.cdc

    def dehydrate_custom_key_name_PASSPORT(self, obj):
        return obj.passport

    def dehydrate_custom_key_name_AGN(self, obj):
        return obj.agn

    def dehydrate_custom_key_name_CNO(self, obj):
        return obj.cno

    def dehydrate_custom_key_name_COMP(self, obj):
        return obj.comp

    def dehydrate_custom_key_name_REMARKS(self, obj):
        return obj.remarks

    def dehydrate_custom_key_name_ID2(self, obj):
        return obj.id


    def dehydrate_custom_key_name_VF(self, obj):
        return obj.vf

    def dehydrate_custom_key_name_VN(self, obj):
        return obj.vn

    def dehydrate_custom_key_name_DOC(self, obj):
        if obj.doc != None:
            return obj.doc.strftime("%d/%m/%Y")
        else:
            ""

    def dehydrate_custom_key_name_SO(self, obj):
        if obj.so != None:
            return obj.so.strftime("%d/%m/%Y")
        else:
            ""

    def dehydrate_custom_key_name_SOF(self, obj):
        if obj.sof != None:
            return obj.sof.strftime("%d/%m/%Y")
        else:
            ""

    def dehydrate_custom_key_name_DOC1(self, obj):
        if obj.doc1!=None:
            return obj.doc1.strftime("%d/%m/%Y")
        else:
            ""

    def dehydrate_custom_key_name_EMAILID(self, obj):
        return obj.emailid

    def dehydrate_custom_key_name_UPDATEDDATE(self, obj):

        if obj.updatedate!=None:
            return obj.updatedate.strftime("%d/%m/%Y %H:%M")
        else:
            ""

