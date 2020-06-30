import requests
from configs.settings import weather_key
from django.http import JsonResponse
from django.shortcuts import render
from django.views import View


class WeatherView(View):

    def get(self, request):
        return render(request, 'index.html')

    def post(self, request):
        city = request.POST['city']
        url = 'http://api.openweathermap.org/data/2.5/forecast?q={}&appid=' + weather_key + '&lang=ru&units=metric'
        get = requests.get(url.format(city)).json()
        if get['cod'] == '200':
            content = get
        else:
            content = {'data': get['message']}
        return JsonResponse(content)
