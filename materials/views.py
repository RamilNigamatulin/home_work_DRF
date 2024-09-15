from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet
from rest_framework.generics import CreateAPIView, ListAPIView, RetrieveAPIView, UpdateAPIView, DestroyAPIView
from materials.models import Course, Lesson
from materials.serializers import CourseSerializer, LessonSerializer, LessonDetailSerializer
from users.permissions import IsModerators, IsOwner


class CourseViewSet(ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer

    def get_permissions(self):
        if self.action == "create":
            self.permission_classes = (~IsModerators,)
        elif self.action in ["update", "retrieve"]:
            self.permission_classes = (IsModerators | IsOwner,)
        elif self.action == "destroy":
            self.permission_classes = (~IsModerators | IsOwner,)
        return super().get_permissions()

    def perform_create(self, serializer):
        "Привязываем текущего пользователя к создаваемому курсу."
        serializer.save(owner=self.request.user)


class LessonCreateApiView(CreateAPIView):
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer
    permission_classes = (~IsModerators, IsAuthenticated)


    def perform_create(self, serializer):
        "Привязываем текущего пользователя к создаваемому уроку."
        serializer.save(owner=self.request.user)


class LessonListApiView(ListAPIView):
    serializer_class = LessonSerializer
    permission_classes = (IsAuthenticated, IsModerators | IsOwner)

    def get_queryset(self):
        queryset = Lesson.objects.all()
        course_id = self.request.query_params.get('course_id')
        if course_id:
            queryset = queryset.filter(course_id=course_id)
        return queryset


class LessonRetrieveApiView(RetrieveAPIView):
    serializer_class = LessonSerializer
    permission_classes = (IsAuthenticated, IsModerators)

    def get_queryset(self):
        queryset = Lesson.objects.all()
        course_id = self.request.query_params.get('course_id')
        if course_id:
            queryset = queryset.filter(course_id=course_id)
        return queryset


class LessonUpdateApiView(UpdateAPIView):
    serializer_class = LessonSerializer
    permission_classes = (IsAuthenticated, IsModerators | IsOwner)

    def get_queryset(self):
        queryset = Lesson.objects.all()
        course_id = self.request.query_params.get('course_id')
        if course_id:
            queryset = queryset.filter(course_id=course_id)
        return queryset


class LessonDestroyApiView(DestroyAPIView):
    serializer_class = LessonSerializer
    permission_classes = (IsAuthenticated, IsOwner | ~IsModerators)

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