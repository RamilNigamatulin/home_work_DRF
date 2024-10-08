# Generated by Django 5.1.1 on 2024-09-15 03:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('materials', '0004_alter_lesson_course'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='owner',
            field=models.CharField(blank=True, help_text='Введите имя владельца курса', max_length=255, null=True, verbose_name='Владелец'),
        ),
        migrations.AddField(
            model_name='lesson',
            name='owner',
            field=models.CharField(blank=True, help_text='Введите имя владельца урока', max_length=255, null=True, verbose_name='Владелец'),
        ),
    ]
