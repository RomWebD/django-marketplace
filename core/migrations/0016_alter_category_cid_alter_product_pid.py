# Generated by Django 5.0.3 on 2024-03-27 14:23

import shortuuid.django_fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0015_alter_vendor_contact'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='cid',
            field=shortuuid.django_fields.ShortUUIDField(alphabet='abcdefgh', editable=False, length=10, max_length=30, prefix='cat', unique=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='pid',
            field=shortuuid.django_fields.ShortUUIDField(alphabet='abcdefgh', editable=False, length=10, max_length=20, prefix='prd', unique=True),
        ),
    ]
