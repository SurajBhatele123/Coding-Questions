# Generated by Django 4.0 on 2022-12-07 03:38

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.CharField(default='', max_length=45)),
                ('lastname', models.CharField(default='', max_length=45)),
                ('dob', models.DateField(default='')),
                ('gender', models.CharField(default='', max_length=7)),
                ('emailid', models.CharField(default='', max_length=45)),
                ('mobile', models.CharField(default='', max_length=12)),
                ('address', models.CharField(default='', max_length=200)),
                ('state', models.CharField(default='', max_length=45)),
                ('city', models.CharField(default='', max_length=45)),
                ('designation', models.CharField(default='', max_length=45)),
                ('managerid', models.IntegerField()),
                ('photograph', models.CharField(default='', max_length=45)),
            ],
        ),
    ]