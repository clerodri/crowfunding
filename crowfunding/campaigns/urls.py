
from django.urls import path
from . import views
app_name = 'campaigns'
urlpatterns = [
    path('', views.campaigns_list, name="list"),
    path('new-campaign', views.campaign_new, name="campaigns-new"),
    path('<slug:id>', views.campaign_page, name="page"),
]