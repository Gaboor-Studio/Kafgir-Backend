# Generated by Django 3.2.5 on 2021-09-03 14:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Kafgir_API', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='requested_otp_password',
            field=models.CharField(max_length=5, null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='requested_otp_time',
            field=models.DateTimeField(null=True),
        ),
    ]
