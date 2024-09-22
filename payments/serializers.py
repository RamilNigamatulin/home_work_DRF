from rest_framework.fields import SerializerMethodField
from rest_framework.serializers import ModelSerializer

from payments.models import Payments


class PaymentsSerializer(ModelSerializer):
    class Meta:
        model = Payments
        fields = ('owner', 'course', 'lesson', 'payment_amount', 'payment_method', 'session_id', 'link',)
