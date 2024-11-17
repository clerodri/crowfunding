from django.db import models
from datetime import date
from django.contrib.auth.models import User
# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=100)
    
    def save(self, *args, **kwargs):
        self.name = self.name.upper()
        super().save(*args, **kwargs)
        
    def __str__(self):
        return f'{self.name}'


class Campaign(models.Model):

    STATE_CHOICES = [
        (1, 'Activo'),
        (0, 'Cerrado'),
    ]
    categories = models.ForeignKey(Category, related_name='campaign_category', on_delete=models.CASCADE, null=True)
    title = models.CharField(max_length=100)
    description = models.TextField()
    direccion = models.CharField(max_length=100)
    profile_img = models.ImageField(upload_to='images_crowfunding/', default='fallback.png', blank=True)
    goal_amount = models.DecimalField(max_digits=10, decimal_places=2)
    current_amount = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    start_date = models.DateField(auto_now_add=True)
    close_date = models.DateField()
    state = models.IntegerField(choices=STATE_CHOICES, default=1)
    user = models.ForeignKey(User, on_delete=models.CASCADE, default= None)
    
    def save(self, *args, **kwargs):
        self.direccion = self.direccion.title()
        if self.current_amount >= self.goal_amount:
            self.state = 0  
        if self.days_remaining() <= 0:
            self.state = 0
        super().save(*args, **kwargs)
        
    def days_remaining(self):
        today = date.today()
        if self.close_date >= today:
            return (self.close_date - today).days
        return 0  
    
    def __str__(self):
        return self.title