import random
import string
from .models import Order

def get_random_string(length):
    result_str = ''.join(random.choice(string.ascii_letters) for i in range(length))
    return result_str

def payment_order_creation(payment_order_details):
    payment_url = f"https://www.streakcard.com/payment/{get_random_string(10)}"
    payment_order = Order.objects.create(
        order_id = payment_order_details.get('order_id'),
        order_amount = payment_order_details.get('order_amount'),
        metadata = payment_order_details.get('order_meta')
    )

    payment_order_info = dict()
    payment_order_info['order_id'] = payment_order.order_id
    payment_order_info['order_amount'] = payment_order.order_amount
    payment_order_info['payment_url'] = payment_url

    return payment_order_info

def fetch_payment_order(order_id):
    payment_order_info = dict()
    try:
        payment_order = Order.objects.get(pk=order_id)
    except Order.DoesNotExist:
        payment_order = None
    
    if payment_order:
        payment_order_info['order_id'] = payment_order.order_id
        payment_order_info['order_status'] = payment_order.order_status

    return payment_order_info
