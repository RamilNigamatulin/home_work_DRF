# Generated by Django 5.1.1 on 2024-09-20 10:28

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('materials', '0008_subscription'),
        ('payments', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='payments',
            name='link',
            field=models.URLField(blank=True, help_text='Ссылка на страницу оплаты', max_length=400, null=True, verbose_name='Ссылка на оплату'),
        ),
        migrations.AddField(
            model_name='payments',
            name='session_id',
            field=models.CharField(blank=True, help_text='Идентификатор сессии платежа', max_length=255, null=True, verbose_name='ID сессии'),
        ),
        migrations.AlterField(
            model_name='payments',
            name='course',
            field=models.ForeignKey(blank=True, help_text='Курс, который был оплачен', null=True, on_delete=django.db.models.deletion.CASCADE, to='materials.course', verbose_name='Оплаченный курс'),
        ),
        migrations.AlterField(
            model_name='payments',
            name='date',
            field=models.DateTimeField(auto_now_add=True, help_text='Дата создания платежа', null=True, verbose_name='Дата оплаты'),
        ),
        migrations.AlterField(
            model_name='payments',
            name='lesson',
            field=models.ForeignKey(blank=True, help_text='Урок, который был оплачен', null=True, on_delete=django.db.models.deletion.CASCADE, to='materials.lesson', verbose_name='Оплаченный урок'),
        ),
        migrations.AlterField(
            model_name='payments',
            name='owner',
            field=models.ForeignKey(help_text='Пользователь, который оплатил', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Пользователь'),
        ),
        migrations.AlterField(
            model_name='payments',
            name='payment_amount',
            field=models.DecimalField(decimal_places=2, help_text='Сумма оплаты в рублях', max_digits=10, verbose_name='Сумма оплаты'),
        ),
        migrations.AlterField(
            model_name='payments',
            name='payment_method',
            field=models.CharField(blank=True, choices=[('cash', 'Наличные'), ('transfer', 'Перевод на счет')], help_text='Выберите способ оплаты', max_length=20, null=True, verbose_name='Способ оплаты'),
        ),
    ]
