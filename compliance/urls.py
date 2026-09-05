from django.urls import path
from .views import CNICView, NTNView, TaxBracketView, ZakatView

urlpatterns = [
    path('validate/cnic/', CNICView.as_view(), name='cnic'),
    path('validate/ntn/', NTNView.as_view(), name='ntn'),
    path("calculate/tax-bracket/", TaxBracketView.as_view(), name='tax-bracket'),
    path("calculate/zakat/", ZakatView.as_view(), name='zakat')
]