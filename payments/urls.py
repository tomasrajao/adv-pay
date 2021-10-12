from django.urls import path

import payments.views
from payments.views import info, send_payment_request

app_name = 'payments'
urlpatterns = [
    path('info/<slug:slug>', info, name='info'),
    path('request/', send_payment_request, name='send_payment_request'),
]
