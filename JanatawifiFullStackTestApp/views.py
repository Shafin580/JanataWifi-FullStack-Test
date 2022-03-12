from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.core import serializers
from .models import StockData
from .forms import StockCreate
from json import dumps

# Create your views here.

def index(request):

    data = StockData.objects.all()
    date = []
    close = []
    volume = []

    for value in data:
        date.append(value.date)
        close.append(value.close)
        volume.append(value.volume)

    print(date)
    dataJSON = serializers.serialize('json', data)
    return render(request, 'index.html', {'data': data, 'date': date, 'close': close, 'volume': volume})

def upload(request):
    upload = StockCreate()
    print(upload)
    if request.method == 'POST':

        upload = StockCreate(request.POST)
        if upload.is_valid():
            upload.save()
            return HttpResponse("New Stock Data Created!")
        else:
            return HttpResponse("Failed to Create New Data!")
    else:
        return render(request, 'upload.html', {'upload_form': upload})

def update(request, stock_id):
    stock_id = int(stock_id)
    try:
        stock = StockData.objects.get(id = stock_id)
    except StockData.DoesNotExist:
        return HttpResponse("Stock Data Does not Exist")
    stock_form = StockCreate(request.POST or None, instance=stock)

    if stock_form.is_valid():
        stock_form.save()
        return HttpResponse("Stock Data Updated!")
    return render(request, 'upload.html', {'upload_form': stock_form})


def delete(request, stock_id):
    stock_id = int(stock_id)
    try:
        stock = StockData.objects.get(id = stock_id)
    except StockData.DoesNotExist:
        return HttpResponse("Stock Data Does not Exist")
    stock.delete()
    return HttpResponse("Stock Data Deleted!")

