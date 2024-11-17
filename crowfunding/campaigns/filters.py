import django_filters
from .models import Campaign,Category

class CampaignFilter(django_filters.FilterSet):
    categories = django_filters.ModelChoiceFilter(
        queryset=Category.objects.all(),
        label="Categoria"
    )

    class Meta:
        model = Campaign
        fields = ['categories']