# Generated by Django 5.0.3 on 2024-03-14 13:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0007_remove_product_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='description',
            field=models.TextField(blank=True, default='This is the product', null=True),
        ),
    ]
