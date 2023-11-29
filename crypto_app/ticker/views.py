from django.shortcuts import render
from .api import get_bitcoin_price

# Create your views here.
# views.py
def home(request):
    btc_price = get_bitcoin_price()  # This should be a raw float, not formatted as a string with currency symbols or commas
    return render(request, 'home.html', {'btc_price': btc_price})

