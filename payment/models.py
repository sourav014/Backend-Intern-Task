from django.db import models
from django.db.models import JSONField
from django.core.serializers.json import DjangoJSONEncoder, Serializer as JsonSerializer
from . import OrderStatus

# Create your models here.

class Serializer(JsonSerializer):
    def _init_options(self):
        super()._init_options()
        self.json_kwargs["cls"] = CustomJsonEncoder


class CustomJsonEncoder(DjangoJSONEncoder):
    def default(self, obj):
        return super().default(obj)

class Order(models.Model):
    order_id = models.CharField(max_length=256, blank=False, null=False, primary_key=True)
    order_amount = models.DecimalField(
        max_digits=12,
        decimal_places=3,
        default=0,
    )
    order_status = models.CharField(
        max_length = 20, choices = OrderStatus.CHOICES, default=OrderStatus.NO_RESPONSE
    )
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True)
    metadata = JSONField(blank=True, null=True, default=dict, encoder=CustomJsonEncoder)

    class Meta:
        ordering = ("pk",)

    def __str__(self):
        return "%s %s" % (self.order_id, self.order_status)
