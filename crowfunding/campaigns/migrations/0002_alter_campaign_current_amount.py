# Generated by Django 5.1.3 on 2024-11-16 20:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('campaigns', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='campaign',
            name='current_amount',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10),
        ),
    ]
