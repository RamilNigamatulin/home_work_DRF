from django.contrib.auth.models import AbstractUser
from django.db import models

from materials.models import Lesson, Course


class User(AbstractUser):
    username = None
    email = models.EmailField(
        unique=True,
        verbose_name='Почта',
        help_text='введите почту',
    )
    phone = models.CharField(
        max_length=15,
        verbose_name='Телефон',
        help_text='Введите номер телефона',
        blank=True,
        null=True,
    )
    city = models.CharField(
        max_length=50,
        verbose_name='Город',
        help_text='Введите город',
        blank=True,
        null=True,
    )
    avatar = models.ImageField(
        blank=True,
        null=True,
        upload_to='photo/avatars/',
        verbose_name='Аватар',
    )

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

    def __str__(self):
        return self.email


class Payments(models.Model):
    user = models.ForeignKey(
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
        return f'{self.user, self.date, self.course, self.lesson, self.payment_amount, self.payment_method}'