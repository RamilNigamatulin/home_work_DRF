from rest_framework.fields import SerializerMethodField
from rest_framework.serializers import ModelSerializer

from materials.models import Course, Lesson


class LessonSerializer(ModelSerializer):
    class Meta:
        model = Lesson
        fields = '__all__'


class CourseSerializer(ModelSerializer):
    lessons = LessonSerializer(many=True, read_only=True)
    number_of_lessons = SerializerMethodField()

    def get_number_of_lessons(self, course):
        return Lesson.objects.filter(course=course).count()


    class Meta:
        model = Course
        fields = ('title', 'description', 'number_of_lessons', 'lessons')


class LessonDetailSerializer(ModelSerializer):
    class Meta:
        model = Lesson
        fields = '__all__'
