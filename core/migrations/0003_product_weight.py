# Generated by Django 5.0.3 on 2024-03-14 13:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_remove_product_tags_alter_productimages_images'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='weight',
            field=models.CharField(default='1kg', max_length=10),
        ),
    ]