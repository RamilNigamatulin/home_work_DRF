from django.db import models
from users.models import User
from materials.models import Course, Lesson


class Payments(models.Model):
    owner = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        verbose_name='Пользователь',
        help_text='Пользователь, который оплатил',
        blank=True,
        null=True,
    )
    date = models.DateTimeField(
        verbose_name='Дата оплаты',
        auto_now_add=True,
        blank=True,
        null=True,
        help_text='Дата создания платежа',
    )
    course = models.ForeignKey(
        Course,
        on_delete=models.CASCADE,
        verbose_name='Оплаченный курс',
        blank=True,
        null=True,
        help_text='Курс, который был оплачен',
    )
    lesson = models.ForeignKey(
        Lesson,
        on_delete=models.CASCADE,
        verbose_name='Оплаченный урок',
        blank=True,
        null=True,
        help_text='Урок, который был оплачен',
    )
    payment_amount = models.PositiveIntegerField(
        verbose_name='Сумма оплаты',
        help_text='Сумма оплаты в рублях',
    )
    payment_method = models.CharField(
        verbose_name='Способ оплаты',
        max_length=20,
        choices=[
            ('cash', 'Наличные'),
            ('transfer', 'Перевод на счет')
        ],
        help_text='Выберите способ оплаты',
        blank=True,
        null=True,
    )
    session_id = models.CharField(
        verbose_name='ID сессии',
        max_length=255,
        help_text='Идентификатор сессии платежа',
        blank=True,
        null=True,
    )
    link = models.URLField(
        verbose_name='Ссылка на оплату',
        max_length=400,
        help_text='Ссылка на страницу оплаты',
        blank=True,
        null=True,
    )

    class Meta:
        verbose_name = 'Платеж'
        verbose_name_plural = 'Платежи'

    def __str__(self):
        return f'{self.owner, self.date, self.course, self.lesson, self.payment_amount, self.payment_method}'
