import requests


def purchase_approve(request):
    """
    KakaoPay 결제 진행
    """
    if request.method == 'POST':
        user = request.user
        data = request.data
