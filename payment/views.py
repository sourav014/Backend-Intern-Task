from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .controllers import payment_order_creation, fetch_payment_order

# Create your views here.
@api_view(['POST'])
def create_payment_order(request):
    if request.method == 'POST':
        data = request.data
        payment_order_data = payment_order_creation(data)
        
        return Response(
            {
                'order_id': payment_order_data.get('order_id'),
                'order_amount': payment_order_data.get('order_amount'),
                'payment_url': payment_order_data.get('payment_url')
            }, 
            status=status.HTTP_200_OK
        )

    else:
        return Response(
            {
                'message': 'Method not allowed'
            }, 
            status=status.HTTP_405_METHOD_NOT_ALLOWED
        )


@api_view(['GET'])
def view_payment_order(request):
    if request.method == 'GET':
        order_id = request.GET.get('order_id')
        payment_order_data = fetch_payment_order(order_id)
        return Response(
            {
                'order_id': payment_order_data.get('order_id'),
                'status': payment_order_data.get('order_status')
            }, 
            status=status.HTTP_200_OK
        )

    else:
        return Response(
            {
                'message': 'Method not allowed'
            }, 
            status=status.HTTP_405_METHOD_NOT_ALLOWED
        )
