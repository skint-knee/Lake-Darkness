from django.shortcuts import render
from django.http import HttpResponse
from pycoingecko import CoinGeckoAPI
# instantiating the coingecko api
cg = CoinGeckoAPI()
# we defined the projects function to require a parameter "pk" or primary key
# these functions are technically views and shouldn't be here
def projects(request, pk):
    return HttpResponse('Here is the basic response {}'.format(pk))
 
def project_form(request):

    msg = cg.get_price(ids='bitcoin', vs_currencies='usd')
    bitcoin_price = msg['bitcoin']['usd']
    f_bitcoin_price = f"The price of Bitcoin is ${bitcoin_price:,.2f}."

    context = {'message':f_bitcoin_price}
    return render(request, 'analyst_form/analyst_form.html', context)