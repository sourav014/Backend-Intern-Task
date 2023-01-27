from django.contrib import admin
from .models import Order

# Register your models here.

@admin.register(Order)
class PaymentOrderAdmin(admin.ModelAdmin):
    list_display = (
        'order_id','order_amount', 'order_status', 'created_at'
    )
    list_filter = ('order_status',)

