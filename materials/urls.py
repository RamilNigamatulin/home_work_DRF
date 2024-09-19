from django.urls import path
from rest_framework.routers import SimpleRouter
from materials.views import (CourseViewSet, LessonCreateApiView, LessonListApiView, LessonUpdateApiView,
                             LessonRetrieveApiView, LessonDestroyApiView, SubscriptionAPIView)
from materials.apps import MaterialsConfig

app_name = MaterialsConfig.name
router = SimpleRouter()
router.register('', CourseViewSet, basename='course')

urlpatterns = [
    path('lessons/', LessonListApiView.as_view(), name='lessons_list'),
    path('lessons/<int:pk>/', LessonRetrieveApiView.as_view(), name='lessons_retrieve'),
    path('lessons/<int:pk>/update/', LessonUpdateApiView.as_view(), name='lessons_update'),
    path('lessons/<int:pk>/delete/', LessonDestroyApiView.as_view(), name='lessons_delete'),
    path('lessons/create/', LessonCreateApiView.as_view(), name='lessons_create'),

    path('subscriptions/', SubscriptionAPIView.as_view(), name='subscriptions'),
]

urlpatterns += router.urls