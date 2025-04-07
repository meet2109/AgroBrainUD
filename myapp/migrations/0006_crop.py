# Generated by Django 5.1.5 on 2025-01-31 19:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0005_tools_badge_tools_collection_tools_img_url_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Crop',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('current_price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('trend', models.CharField(choices=[('UP', 'Increasing'), ('DOWN', 'Decreasing'), ('STABLE', 'Stable')], max_length=10)),
                ('historical_prices', models.JSONField(default=dict)),
                ('description', models.TextField(blank=True)),
                ('image', models.ImageField(blank=True, upload_to='crops/')),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
