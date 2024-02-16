from django.shortcuts import render
import requests


def exchange(request):
    response = requests.get('https://v6.exchangerate-api.com/v6/b9a75adf8812e86afe5e5b87/latest/USD').json()
    currensies = response.get('conversion_rates')

    if request.method == 'GET':
        context = {
            'currensies': currensies
        }

        return render(request=request, template_name='exchange/index.html', context=context)

    if request.method == 'POST':
        from_amount = request.POST.get('from_amount')
        from_curr = request.POST.get('from_curr')
        to_curr = request.POST.get('to_curr')

        converted_amount = round((float(from_amount) * (currensies[to_curr] / currensies[from_curr])), 2)

        context ={
            'currensies': currensies,
            'converted_amount': converted_amount,
            'from_amount': from_amount,
            'from_curr':from_curr,
            'to_curr':to_curr
        }

        return render(request=request, template_name='exchange/index.html', context=context)
