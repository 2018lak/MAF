from import_export import resources, widgets
from import_export.fields import Field
from .models import Data

class DataResource(resources.ModelResource):
    date = Field(attribute='date', column_name=u'거래일시')
    type = Field(attribute='type', column_name=u'구분', widget=widgets.CharWidget())
    store = Field(attribute='store', column_name=u'적요', widget=widgets.CharWidget())
    withdraw = Field(attribute='withdraw', column_name=u'출금액', widget=widgets.IntegerWidget())
    deposit = Field(attribute='deposit', column_name=u'입금액', widget=widgets.IntegerWidget())
    total = Field(attribute='total', column_name=u'잔액', widget=widgets.CharWidget())
    type2 = Field(attribute='type2', column_name=u'거래점', widget=widgets.CharWidget())

    class Meta:
        model = Data