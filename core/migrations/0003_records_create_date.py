# Generated by Django 3.0.6 on 2020-06-07 13:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_auto_20200602_1632'),
    ]

    operations = [
        migrations.AddField(
            model_name='records',
            name='create_date',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
