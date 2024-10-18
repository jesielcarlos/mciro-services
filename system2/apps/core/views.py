# orders/views.py
from django.http import JsonResponse
from django.views import View
from .services import OrderService
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
import json

class OrderView(View):
    service = OrderService()

    @method_decorator(csrf_exempt)
    def post(self, request):
        data = json.loads(request.body)
        order = self.service.create_order(data['user_id'], data['items'])
        return JsonResponse({'id': order.id, 'user_id': order.user_id, 'items': order.items})
