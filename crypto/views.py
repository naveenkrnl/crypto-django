from django.shortcuts import render
import requests
import json
# Create your views here.

def home(request):

    #Grrab Crypto Price Data
    price_request=requests.get("https://min-api.cryptocompare.com/data/pricemultifull?fsyms=BTC,ETH,XRP,BCH,EOS,LTC,XLM,ADA,USDT,MIOTA,TRX&tsyms=USD")
    price=json.loads(price_request.content)
    #Grab Crypto News
    api_request=requests.get("https://min-api.cryptocompare.com/data/v2/news/?lang=EN")
    api=json.loads(api_request.content)
    return render(request,'home.html',{'api':api,'price':price})
     

def prices(request):
    context={}
    if request.method=="POST":
        quote=request.POST.get('quote')
        quote=quote.upper()
        print(request.POST)
        #Grrab Crypto Price Data
        crypto_request=requests.get("https://min-api.cryptocompare.com/data/pricemultifull?fsyms={}&tsyms=USD".format(quote))
        crypto=json.loads(crypto_request.content)
        context['crypto']=crypto
    else:
        context['a']='a'
    return render(request, 'prices.html',context)