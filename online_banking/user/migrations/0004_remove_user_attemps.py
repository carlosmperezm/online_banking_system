# Generated by Django 5.0.4 on 2024-04-27 22:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0003_user_balance'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='attemps',
        ),
    ]
