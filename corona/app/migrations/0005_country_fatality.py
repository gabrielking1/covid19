# Generated by Django 3.2.18 on 2023-02-16 19:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_country'),
    ]

    operations = [
        migrations.AddField(
            model_name='country',
            name='Fatality',
            field=models.CharField(default=True, max_length=50),
            preserve_default=False,
        ),
    ]
