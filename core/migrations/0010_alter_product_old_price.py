# Generated by Django 5.0.3 on 2024-03-14 15:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0009_product_vendor'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='old_price',
            field=models.DecimalField(decimal_places=2, max_digits=9999, null=True),
        ),
    ]
