from datetime import timedelta

from django.utils import timezone

from celery import shared_task
from dateutil.utils import today

from config.settings import EMAIL_HOST_USER
from django.core.mail import send_mail
from users.models import User


@shared_task
def information_subscription_off(email, course_title):
    """Отправлем письмо о прекращении подписки."""
    send_mail(
        'Обновление курса',
        f'Внимание, подписка на курс {course_title} прекращена!',
        EMAIL_HOST_USER,
        [email],
    )


@shared_task
def information_subscription_on(email, course_title):
    """Отправлем письмо о подключении подписки."""
    send_mail(
        'Обновление курса',
        f'Внимание, подписка на курс {course_title} оформлена!',
        EMAIL_HOST_USER,
        [email],
    )

@shared_task
def block_users():
    """Блокирует пользователя, который не заходил более 1 месяца."""
    one_month_ago = timezone.now() - timedelta(days=30)
    users = User.objects.filter(last_login__lt=one_month_ago, is_active=True, is_superuser=False)
    for user in users:
        user.is_active = False
        user.save()
