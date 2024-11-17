from django.db import models
from django.contrib.auth.models import User
from campaigns.models import Campaign


class Donation(models.Model):
    campaign = models.ForeignKey(Campaign, related_name='donations', on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    date_donated = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Donation of ${self.amount} by {self.user} to {self.campaign.title}"
