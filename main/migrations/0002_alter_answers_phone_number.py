# Generated by Django 4.1.4 on 2023-11-21 19:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='answers',
            name='phone_number',
            field=models.CharField(default='0000000000', max_length=15, unique=True),
        ),
    ]
