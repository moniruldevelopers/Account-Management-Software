# Generated by Django 5.1.7 on 2025-03-14 07:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0010_alter_profile_profile_picture'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='profile_picture',
            field=models.ImageField(blank=True, null=True, upload_to='profile_pics/'),
        ),
    ]
