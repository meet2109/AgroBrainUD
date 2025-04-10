# Generated by Django 5.1.5 on 2025-01-31 17:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0004_tools_delete_tool'),
    ]

    operations = [
        migrations.AddField(
            model_name='tools',
            name='badge',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='tools',
            name='collection',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AddField(
            model_name='tools',
            name='img_url',
            field=models.URLField(default=''),
        ),
        migrations.AddField(
            model_name='tools',
            name='link',
            field=models.URLField(default=''),
        ),
        migrations.AddField(
            model_name='tools',
            name='new_price',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10),
        ),
        migrations.AddField(
            model_name='tools',
            name='old_price',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10),
        ),
        migrations.AddField(
            model_name='tools',
            name='rating',
            field=models.IntegerField(default=0),
        ),
    ]
