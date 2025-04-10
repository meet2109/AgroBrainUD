# Generated by Django 5.1.7 on 2025-03-21 19:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0009_planthealthreport'),
    ]

    operations = [
        migrations.AlterField(
            model_name='planthealthreport',
            name='confidence_level',
            field=models.CharField(max_length=10),
        ),
        migrations.AlterField(
            model_name='planthealthreport',
            name='image',
            field=models.ImageField(default='default.JPG', upload_to='plant_reports/'),
        ),
        migrations.AlterField(
            model_name='planthealthreport',
            name='plant_health',
            field=models.CharField(max_length=50),
        ),
    ]
