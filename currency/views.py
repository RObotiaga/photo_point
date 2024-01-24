import datetime
from django_ratelimit.decorators import ratelimit
from django.http import JsonResponse
import freecurrencyapi
from decouple import config
from django.views.decorators.http import require_http_methods

client = freecurrencyapi.Client(config('FREECURRENCYAPI'))
last_10_requests = []


@require_http_methods(["GET"])
@ratelimit(key='user', rate='1/10s', method=['GET'], block=True)
def get_current_usd(request):
    # Записываем время перед отправкой запроса
    request_time = datetime.datetime.now()

    # Запрос курса доллара к рублю
    response = client.latest(currencies=['RUB'])['data']['RUB']
    response = {"rate": response, "request_time": request_time}

    # Добавление текущего запроса в список
    last_10_requests.append(response)

    # Ограничение списка последних 10 запросов
    if len(last_10_requests) > 10:
        last_10_requests.pop(0)

    return JsonResponse({
        'current_usd_rate': response,
        'history_requests': last_10_requests
    })
