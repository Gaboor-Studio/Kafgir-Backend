# Generated by Django 3.2.5 on 2021-10-04 15:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Kafgir_API', '0012_history'),
    ]

    operations = [
        migrations.AddField(
            model_name='history',
            name='category',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='Kafgir_API.tag'),
        ),
    ]