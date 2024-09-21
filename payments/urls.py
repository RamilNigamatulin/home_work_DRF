from django.urls import path
from rest_framework.routers import SimpleRouter
from payments.models import Payments
from payments.views import (PaymentsCreateAPIView, PaymentsListAPIView,) # PaymentsDestroyAPIView, PaymentsUpdateAPIView,
                         #PaymentsRetrieveAPIView
from payments.apps import PaymentsConfig


app_name = PaymentsConfig.name

urlpatterns = [
    path('payments/', PaymentsListAPIView.as_view(), name='payments_list'),
    path('create/', PaymentsCreateAPIView.as_view(), name='payments_create'),
]
