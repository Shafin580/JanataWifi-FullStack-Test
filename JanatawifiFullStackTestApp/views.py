from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .models import StockData
from .forms import StockCreate
from datetime import datetime
from django.core.paginator import Paginator
import pandas as pd
import json

# Create your views here.

def create(request):
    data = pd.read_csv('JanatawifiFullStackTestApp\data\stock_market_data.csv')
    json_records = data.reset_index().to_json(orient ='records')
    rowData = []
    rowData = json.loads(json_records)
    for d in rowData:
        #print(d['date'])
        StockData.objects.create(date=d['date'], trade_code = d['trade_code'], high = d['high'], low = d['low'], open = d['open'], close = d['close'], volume = d['volume'])
    return HttpResponse("Full Data Created!")

def index(request):

    data = Paginator(StockData.objects.all(), 10)
    page = request.GET.get('page')
    pagedData = data.get_page(page)
    date = []
    close = []
    volume = []
    trade_code = []
    high = []
    low = []

    for value in pagedData:
        date.append(value.date.strftime("%m/%d/%Y"))
        close.append(value.close)
        volume.append(value.volume)
        trade_code.append(value.trade_code)
        high.append(value.high)
        low.append(value.low)

    return render(request, 'index.html', {'date': date, 'close': close, 'volume': volume, 'trade_code': trade_code, 'high': high, 'low': low, 'pages': pagedData})

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

