from django.shortcuts import render
from django.http import JsonResponse
import urllib.request
import json

def index(request):
    return render(request, 'index.html')

def get_rates(request):
    base = request.GET.get('base', 'USD')
    allowed = ['USD','EUR','RUB','KGS','CNY','KZT','UZS','TRY','GBP','AED']
    if base not in allowed:
        base = 'USD'
    try:
        # Этот API поддерживает KGS и все нужные валюты — бесплатно
        url = f'https://open.er-api.com/v6/latest/{base}'
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        with urllib.request.urlopen(req, timeout=5) as r:
            data = json.loads(r.read())
        
        # Фильтруем только нужные валюты
        filtered = {k: v for k, v in data['rates'].items() if k in allowed}
        return JsonResponse({'base': base, 'rates': filtered})
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=500)