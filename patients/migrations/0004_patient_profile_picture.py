# Generated by Django 4.2.4 on 2023-08-19 10:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('patients', '0003_alter_patient_email_alter_patient_phone'),
    ]

    operations = [
        migrations.AddField(
            model_name='patient',
            name='profile_picture',
            field=models.ImageField(default='/icon/profile.jpg', upload_to='patients_profile_picture'),
        ),
    ]
