from django.shortcuts import render, redirect
from .models import Campaign
from django.contrib.auth.decorators import login_required, user_passes_test
from . import forms
from .filters import CampaignFilter
# Create your views here.
def is_admin(user):
    return user.groups.filter(name='Administrator').exists()

def campaigns_list(request):      
   campaigns = Campaign.objects.all()
   campaign_filter = CampaignFilter(request.GET, queryset=campaigns)
   return render(request, 'campaigns_list.html', {'filter': campaign_filter})


def campaign_page(request, id):
   if request.user.is_authenticated:
        campaign = Campaign.objects.get(id=id)
        return  render(request, 'campaign_page.html', {'campana': campaign})
   else:
      return redirect('users:login');

@login_required(login_url="/users/login/")
@user_passes_test(is_admin, login_url='/login/')
def campaign_new(request):
   if request.method == 'POST':
      form = forms.CreateCampaign(request.POST, request.FILES)
      if form.is_valid():
         newCampaign = form.save(commit=False)
         newCampaign.user = request.user
         newCampaign.save()
         return redirect('campaigns:list');
   else:
      form = forms.CreateCampaign()
   return render(request, 'campaign_new.html',{'form': form})