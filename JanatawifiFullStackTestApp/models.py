from django.db import models
from django.utils import timezone


class StockData(models.Model):
    date = models.DateField(('date'), default=timezone.now)
    trade_code = models.CharField(('trade_code'), max_length=150)
    high = models.FloatField(('high'))
    low = models.FloatField(('low'))
    open = models.FloatField(('open'))
    close = models.FloatField(('close'))
    volume = models.BigIntegerField(('volume'))
