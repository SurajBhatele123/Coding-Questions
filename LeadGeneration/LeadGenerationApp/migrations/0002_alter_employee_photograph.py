# Generated by Django 4.0 on 2022-12-11 08:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('LeadGenerationApp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='photograph',
            field=models.ImageField(upload_to='static/'),
        ),
    ]