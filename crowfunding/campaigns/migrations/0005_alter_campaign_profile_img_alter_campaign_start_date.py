# Generated by Django 5.1.3 on 2024-11-17 03:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('campaigns', '0004_alter_campaign_profile_img'),
    ]

    operations = [
        migrations.AlterField(
            model_name='campaign',
            name='profile_img',
            field=models.ImageField(blank=True, default='fallback.png', upload_to='images_crowfunding/'),
        ),
        migrations.AlterField(
            model_name='campaign',
            name='start_date',
            field=models.DateField(auto_now_add=True),
        ),
    ]
