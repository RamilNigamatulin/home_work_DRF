from rest_framework.viewsets import ModelViewSet
from rest_framework.generics import CreateAPIView, ListAPIView, RetrieveAPIView, UpdateAPIView, DestroyAPIView
from materials.models import Course, Lesson
from materials.serializers import CourseSerializer, LessonSerializer, LessonDetailSerializer


class CourseViewSet(ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer


class LessonCreateApiView(CreateAPIView):
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer

    def get_serializer_class(self):
        if self.action=='retrieve':
            return LessonDetailSerializer
        return LessonSerializer


class LessonListApiView(ListAPIView):
    serializer_class = LessonSerializer

    def get_queryset(self):
        queryset = Lesson.objects.all()
        course_id = self.request.query_params.get('course_id')
        if course_id:
            queryset = queryset.filter(course_id=course_id)
        return queryset


class LessonRetrieveApiView(RetrieveAPIView):
    serializer_class = LessonSerializer

    def get_queryset(self):
        queryset = Lesson.objects.all()
        course_id = self.request.query_params.get('course_id')
        if course_id:
            queryset = queryset.filter(course_id=course_id)
        return queryset


class LessonUpdateApiView(UpdateAPIView):
    serializer_class = LessonSerializer

    def get_queryset(self):
        queryset = Lesson.objects.all()
        course_id = self.request.query_params.get('course_id')
        if course_id:
            queryset = queryset.filter(course_id=course_id)
        return queryset


class LessonDestroyApiView(DestroyAPIView):
    serializer_class = LessonSerializer

    def get_queryset(self):
        # Получаем все объекты модели Lesson из базы данных
        queryset = Lesson.objects.all()

        # Получаем значение параметра 'course_id' из query_params запроса
        course_id = self.request.query_params.get('course_id')

        # Если параметр 'course_id' присутствует в запросе
        if course_id:
            # Фильтруем queryset, чтобы получить только уроки, связанные с указанным курсом
            queryset = queryset.filter(course_id=course_id)

        # Возвращаем отфильтрованный queryset
        return queryset