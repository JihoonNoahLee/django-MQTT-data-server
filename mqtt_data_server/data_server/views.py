from django.shortcuts import render

# Create your views here.
from data_server.models import Data
from rest_framework.response import Response
from rest_framework.views import APIView
from django.views.generic import View
from time import mktime, strptime

class DataAPIView(APIView):
    
    authentication_classes = []
    permission_classes = []

    def get(self, request):
        Database = Data.objects.all().order_by('date')
        temperature_list = []
        humidity_list = []
        for datas in Database:
            time_tuple = strptime(str(datas.date), '%Y-%m-%d %H:%M:%S%z')
            utc_now = mktime(time_tuple) *1000
            temperature_list.append([utc_now, datas.temperature])
            humidity_list.append([utc_now, datas.humidity])


        data = {
            'temperature': temperature_list,
            'humidity': humidity_list
        }

        return Response(data)

class CharView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'data_server/main.html')