import os
import requests

from django.shortcuts import render
from django.shortcuts import redirect


def index(request):
    if request.method == 'POST':
        res = requests.post('http://127.0.0.1:8000/purchases/ready/', data={'product_pk': 63, 'quantity': 1})
        res_data = res.json()
        return redirect(res_data.get('next_redirect_pc_url'))
    return render(request, 'kakaopay/index.html')
