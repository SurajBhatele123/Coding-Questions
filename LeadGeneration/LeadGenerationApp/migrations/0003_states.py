# Generated by Django 4.0 on 2022-12-13 12:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('LeadGenerationApp', '0002_alter_employee_photograph'),
    ]

    operations = [
        migrations.CreateModel(
            name='States',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('stateid', models.IntegerField()),
                ('statename', models.CharField(default='', max_length=45)),
            ],
        ),
    ]
