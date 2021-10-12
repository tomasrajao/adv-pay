from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from rolepermissions.checkers import has_object_permission

from payments import facade
from payments.forms import PaymentForm
from payments.models import Company


def send_payment_request(request):
    form = PaymentForm(request.POST or None)
    if form.is_valid():
        form.save()
    return render(request, 'payments/payment_request.html', {'form': form})


def info(request, slug):
    company = Company.objects.get(slug=slug)
    if has_object_permission('company_content', request.user, company):
        return render(request, 'payments/info.html', context={'company': company})
    return render(request, 'base/home.html')

