from django import forms
from .models import StockData

class StockCreate(forms.ModelForm):
    class Meta:
        model = StockData
        fields = ('id','date','trade_code','high','low','open','close','volume')

        widgets = {
            'id': forms.HiddenInput(),
            'date': forms.DateInput(attrs={'class': 'form-control'}),
            'trade_code': forms.TextInput(attrs={'class': 'form-control'}),
            'high': forms.NumberInput(attrs={'class': 'form-control'}),
            'low': forms.NumberInput(attrs={'class': 'form-control'}),
            'open': forms.NumberInput(attrs={'class': 'form-control'}),
            'close': forms.NumberInput(attrs={'class': 'form-control'}),
            'volume': forms.NumberInput(attrs={'class': 'form-control'})
        }