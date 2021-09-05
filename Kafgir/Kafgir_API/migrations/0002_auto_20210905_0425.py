# Generated by Django 3.2.5 on 2021-09-04 23:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Kafgir_API', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='food',
            name='rating_count',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='ingredient',
            name='name',
            field=models.CharField(max_length=255, unique=True),
        ),
    ]