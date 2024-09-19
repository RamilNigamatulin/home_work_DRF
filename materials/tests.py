from http.client import responses

from django.db.models.expressions import result
from django.template.defaultfilters import title
from django.urls import reverse
from rest_framework.test import APITestCase

from materials.models import Lesson, Course, Subscription
from users.models import User
from rest_framework import status
from django.contrib.auth.models import Group


class MaterialsNrTestCase(APITestCase):

    def setUp(self):
        self.user = User.objects.create(email='test@test.ru')
        self.moderator_group, _ = Group.objects.get_or_create(name='moderators')
        self.user.groups.add(self.moderator_group)
        self.lesson = Lesson.objects.create(title='Урок_1', description='описание урока Урок_1', owner=self.user)
        self.course = Course.objects.create(title='Курс_1', description='описание курса Курс_1', owner=self.user)
        self.client.force_authenticate(user=self.user)

    def test_lesson_retrieve(self):
        url = reverse("materials:lessons_retrieve", args=(self.lesson.pk,))
        response = self.client.get(url)
        data = response.json()
        self.assertEquals(
            response.status_code, status.HTTP_200_OK
        )
        self.assertEquals(
            data.get("title"), self.lesson.title
        )

    def test_lesson_create(self):
        self.user.groups.remove(self.moderator_group)
        url = reverse("materials:lessons_create", )
        data = {
            "title": "Урок_2",
            "description": "описание урока Урок_2",
        }
        response = self.client.post(url, data)
        self.assertEquals(
            response.status_code, status.HTTP_201_CREATED
        )
        self.assertEquals(
            Lesson.objects.all().count(), 2
        )

    def test_lesson_update(self):
        url = reverse("materials:lessons_update", args=(self.lesson.pk,))
        data = {
            "title": "Урок_2",
            "description": "описание урока Урок_2",
        }
        response = self.client.patch(url, data)
        data = response.json()
        self.assertEquals(
            response.status_code, status.HTTP_200_OK
        )
        self.assertEquals(
            data.get("title"), "Урок_2"
        )

    def test_lesson_delete(self):
        url = reverse("materials:lessons_delete", args=(self.lesson.pk,))
        response = self.client.delete(url)
        self.assertEquals(
            response.status_code, status.HTTP_204_NO_CONTENT
        )
        self.assertEquals(
            Lesson.objects.all().count(), 0
        )

    def test_lesson_list(self):
        self.user.groups.remove(self.moderator_group)
        url = reverse("materials:lessons_list", )
        response = self.client.get(url)
        data = response.json()
        result = {
            "count": 1,
            "next": None,
            "previous": None,
            "results": [
                {
                    "id": self.lesson.pk,
                    "title": self.lesson.title,
                    "description": self.lesson.description,
                    "preview": None,
                    "video_link": None,
                    "course": None,
                    "owner": self.user.pk
                }
            ]
        }
        self.assertEquals(
            response.status_code, status.HTTP_200_OK
        )
        self.assertEquals(
            data, result
        )

    def test_subscription_create(self):
        course = Course.objects.create(title='Курс_2', description='описание курса Курс_2', owner=self.user)
        url = reverse("materials:subscriptions")
        data = {
            "course_id": course.id
        }
        response = self.client.post(url, data)
        self.assertEquals(
            response.status_code, status.HTTP_200_OK
        )
        self.assertTrue(response.json().get("is_subscribed"))
        self.assertTrue(Subscription.objects.filter(owner=self.user, course=course).exists())

    def test_subscription_delete(self):
        course = Course.objects.create(title='Курс_2', description='описание курса Курс_2', owner=self.user)
        Subscription.objects.create(owner=self.user, course=course)
        url = reverse("materials:subscriptions")
        data = {
            "course_id": course.id
        }
        response = self.client.post(url, data)
        self.assertEquals(
            response.status_code, status.HTTP_200_OK
        )
        self.assertFalse(response.json().get("is_subscribed"))
        self.assertFalse(Subscription.objects.filter(owner=self.user, course=course).exists())