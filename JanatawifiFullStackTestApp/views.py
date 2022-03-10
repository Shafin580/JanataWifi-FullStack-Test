from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
import csv
import json
import pandas as pd

# Create your views here.

def index(request):

    data = pd.read_csv('JanatawifiFullStackTestApp\data\stock_market_data.csv')
    json_records = data.reset_index().to_json(orient ='records')
    rowData = []
    rowData = json.loads(json_records)
    return render(request, 'index.html', {'data': data, 'rows': rowData})

