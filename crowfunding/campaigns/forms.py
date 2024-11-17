from django import forms 
from . import models

class CreateCampaign(forms.ModelForm):
    class Meta:
        model = models.Campaign
        fields = ['categories','title','description','profile_img','goal_amount','direccion','close_date']
        labels = {
            'categories': 'Categoria',
            'title': 'Titulo',
            'description': 'Detalles de campaña',
            'profile_img': 'Imagen de campaña',
            'goal_amount': 'Meta',
            'direccion': 'Localidad',
            'close_date': 'Fecha de cierre',
        }