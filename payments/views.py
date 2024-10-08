from requests import session
from rest_framework.viewsets import ModelViewSet
from rest_framework.generics import CreateAPIView, ListAPIView, RetrieveAPIView, UpdateAPIView, DestroyAPIView
from payments.models import Payments
from payments.serializers import PaymentsSerializer
from rest_framework import filters
from django_filters.rest_framework import DjangoFilterBackend

from payments.services import create_stripe_session, create_stripe_price, \
    create_stripe_product  # convert_rub_to_dollars,


class PaymentsListAPIView(ListAPIView):
    queryset = Payments.objects.all()
    serializer_class = PaymentsSerializer
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter]
    ordering_fields = ('date',)
    filterset_fields = ('id', 'course', 'lesson', 'payment_method')


class PaymentsCreateAPIView(CreateAPIView):
    queryset = Payments.objects.all()
    serializer_class = PaymentsSerializer

    def perform_create(self, serializer):
        payment = serializer.save(owner=self.request.user)
        product = create_stripe_product(payment.course)
        price = create_stripe_price(product.id, payment.payment_amount)
        session_id, payment_link = create_stripe_session(price.id)
        payment.session_id = session_id
        payment.link = payment_link
        payment.save()
