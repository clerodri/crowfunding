from django.shortcuts import render, redirect, get_object_or_404
from campaigns.models import Campaign
from .form import DonationForm
from django.contrib.auth.decorators import login_required
from django.db import transaction

@login_required
@transaction.atomic
def make_donation(request, campaign_id):
    campaign = get_object_or_404(Campaign, id=campaign_id)

    if request.method == "POST":
        form = DonationForm(request.POST)
        if form.is_valid():
            donation = form.save(commit=False)
            donation.campaign = campaign
            donation.user = request.user
            donation.save()
            campaign.current_amount += donation.amount
            campaign.save()
            return redirect('campaigns:list')  # Redirect to a relevant page after donation
    else:
        form = DonationForm()

    return render(request, 'donations/donation.html', {'form': form, 'campaign': campaign})
