from django.db import models
from users.models import User


class Course(models.Model):
    title = models.CharField(
        max_length=255,
        verbose_name='Название курса',
        help_text='Введите название курса',
    )
    description = models.TextField(
        verbose_name='Описание курса',
        help_text='Введите описание курса',
    )
    preview = models.ImageField(
        blank=True,
        null=True,
        upload_to='photo/course/',
        verbose_name='картинка',
    )
    owner = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        verbose_name='Пользователь',
    )


    class Meta:
        verbose_name = 'Курс'
        verbose_name_plural = 'Курсы'

    def __str__(self):
        return f'{self.title}, {self.owner}'


class Lesson(models.Model):
    course = models.ForeignKey(
        Course,
        related_name='lessons',
        on_delete=models.CASCADE,
        verbose_name='Курс',
        blank=True,
        null=True,
    )
    title = models.CharField(
        max_length=255,
        verbose_name='Название урока',
        help_text='Введите название урока',
    )
    description = models.TextField(
        verbose_name='Описание урока',
        help_text='Введите описание урока',
    )
    preview = models.ImageField(
        blank=True,
        null=True,
        upload_to='photo/lesson/',
        verbose_name='картинка',
    )
    video_link = models.CharField(
        blank=True,
        null=True,
        max_length=255,
        verbose_name='Ссылка на видео',
        help_text='Введите ссылку на видео',
    )
    owner = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        verbose_name='Пользователь',
    )


    class Meta:
        verbose_name = 'Урок'
        verbose_name_plural = 'Уроки'

    def __str__(self):
        return f'{self.title}, {self.owner}'


class Subscription(models.Model):
    course = models.ForeignKey(
        Course,
        on_delete=models.CASCADE,
        verbose_name='Курс',
        blank=True,
        null=True,
    )
    owner = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        verbose_name='Пользователь',
    )

    class Meta:
        verbose_name = 'Подписка'
        verbose_name_plural = 'Подписки'

    def __str__(self):
        return f'{self.course}, {self.owner}'
