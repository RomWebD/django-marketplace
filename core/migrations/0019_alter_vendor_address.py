# Generated by Django 5.0.3 on 2024-03-27 14:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0018_alter_vendor_contact'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vendor',
            name='address',
            field=models.GenericIPAddressField(default='1 Main Street.'),
        ),
    ]
