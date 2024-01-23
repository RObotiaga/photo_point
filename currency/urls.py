from django.urls import path
from .apps import CurrencyConfig
from .views import get_current_usd

app_name = CurrencyConfig.name

urlpatterns = [
    path('get-current-usd/', get_current_usd, name='get_current_usd'),
]
