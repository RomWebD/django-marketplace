# Generated by Django 5.0.3 on 2024-03-07 13:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userauths', '0003_alter_user_bio'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='bio',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
    ]
