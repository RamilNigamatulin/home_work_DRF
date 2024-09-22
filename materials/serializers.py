from rest_framework.fields import SerializerMethodField
from rest_framework.serializers import ModelSerializer
from .validators import VideoLinkValidator

from materials.models import Course, Lesson, Subscription


class LessonSerializer(ModelSerializer):
    class Meta:
        model = Lesson
        fields = '__all__'
        read_only_fields = ['owner']
        validators = [VideoLinkValidator(field='video_link')]

class CourseSerializer(ModelSerializer):
    lessons = LessonSerializer(many=True, read_only=True)
    number_of_lessons = SerializerMethodField()
    is_subscribed = SerializerMethodField()

    def get_number_of_lessons(self, course):
        return Lesson.objects.filter(course=course).count()

    def get_is_subscribed(self, course):
        user = self.context['request'].user
        return Subscription.objects.filter(course=course, owner=user).exists()

    class Meta:
        model = Course
        fields = ('id', 'title', 'description', 'number_of_lessons', 'lessons', 'owner', 'is_subscribed',)
        read_only_fields = ['owner']

class LessonDetailSerializer(ModelSerializer):
    class Meta:
        model = Lesson
        fields = '__all__'


class SubscriptionSerializer(ModelSerializer):
    class Meta:
        model = Subscription
        fields = ('course', 'owner',)
