# Generated by Django 5.0.3 on 2024-03-27 14:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0017_alter_vendor_contact'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vendor',
            name='contact',
            field=models.CharField(default='+380 069 412 4100', max_length=15),
        ),
    ]