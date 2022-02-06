import requests


def purchase_ready(request):
    """
    KakaoPay 결제 준비
    """
    if request.method == 'POST':
        user = request.user
        data = request.data
