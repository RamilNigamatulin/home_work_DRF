# Generated by Django 5.1.1 on 2024-09-15 05:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_rename_user_payments_owner'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Payments',
        ),
    ]
