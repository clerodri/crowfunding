
from django.urls import path
from .views import make_donation
app_name = 'donations'
urlpatterns = [
   path('<int:campaign_id>/', make_donation, name='make_donation'),
]