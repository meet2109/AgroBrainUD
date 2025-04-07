# Generated by Django 5.1.5 on 2025-02-01 16:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0007_remove_crop_historical_prices_remove_crop_image_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='ResourceItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(choices=[('seeds', 'Seeds and Plants'), ('fertilizers', 'Fertilizers and Soil Amendments'), ('pest_control', 'Pesticides and Pest Control'), ('livestock', 'Livestock and Animal Care'), ('storage', 'Storage Solutions')], default='seeds', max_length=20)),
                ('title', models.CharField(max_length=200)),
                ('link', models.URLField()),
                ('img_url', models.URLField(verbose_name='Image URL')),
                ('price_range', models.CharField(max_length=100)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'Resource Item',
                'verbose_name_plural': 'Resource Items',
                'ordering': ['-created_at'],
            },
        ),
    ]
