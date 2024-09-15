from django.db import models
from users.models import User
from materials.models import Course, Lesson


class Payments(models.Model):
    owner = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        verbose_name='Пользователь',
    )
    date = models.DateTimeField(
        verbose_name='Дата оплаты',
        auto_now_add=True,
        blank=True,
        null=True,
    )
    course = models.ForeignKey(
        Course,
        on_delete=models.CASCADE,
        verbose_name='Оплаченный курс',
        blank=True,
        null=True,
    )
    lesson = models.ForeignKey(
        Lesson,
        on_delete=models.CASCADE,
        verbose_name='Оплаченный урок',
        blank=True,
        null=True,
    )
    payment_amount = models.DecimalField(
        verbose_name='Сумма оплаты',
        max_digits=10,
        decimal_places=2,
    )
    payment_method = models.CharField(
        verbose_name='Способ оплаты',
        max_length=20,
        choices=[
            ('cash', 'Наличные'),
            ('transfer', 'Перевод на счет')
        ]
    )


    class Meta:
        verbose_name = 'Платеж'
        verbose_name_plural = 'Платежи'

    def __str__(self):
        return f'{self.owner, self.date, self.course, self.lesson, self.payment_amount, self.payment_method}'
