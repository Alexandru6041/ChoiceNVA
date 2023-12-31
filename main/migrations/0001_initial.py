# Generated by Django 4.1.4 on 2023-11-21 18:01

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Answers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('prenume', models.CharField(max_length=100)),
                ('family_name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=100, unique=True)),
                ('phone_number', models.CharField(max_length=15, unique=True)),
                ('message', models.CharField(max_length=3750)),
                ('public_ip_address', models.GenericIPAddressField(unique=True)),
                ('has_submitted_cookie', models.BooleanField(default=False)),
            ],
        ),
    ]
