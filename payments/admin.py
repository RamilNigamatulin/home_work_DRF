from django.contrib import admin
from payments.models import Payments

@admin.register(Payments)
class Payments(admin.ModelAdmin):
    list_display = ('id', 'owner', 'date', 'course', 'lesson', 'payment_amount', 'payment_method')
    list_filter = ('id', 'owner',)

# Register your models here.
