from uuid import uuid4

from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.db import models
from django.template.defaultfilters import slugify


def only_int(value):
    if value.isdigit() == False:
        raise ValidationError('ID contém caracteres.')


class Company(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    company_name = models.CharField(max_length=64)
    slug = models.SlugField(unique=True)
    CNPJ = models.CharField(max_length=14, validators=[only_int])

    def __str__(self):
        return self.company_name


class Supplier(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    supplier_name = models.CharField(max_length=64)
    slug = models.SlugField(unique=True)
    CNPJ = models.CharField(max_length=14, validators=[only_int])

    def __str__(self):
        return self.supplier_name


STATUS_CHOICES = (
    (0, 'unrequested'),
    (1, 'in progress'),
    (2, 'canceled'),
    (3, 'aproved'),
)


class Payment(models.Model):
    payment_id = models.AutoField(primary_key=True, editable=False)
    supplier = models.ForeignKey('Supplier', on_delete=models.PROTECT)
    company = models.ForeignKey('Company', on_delete=models.PROTECT)
    issue_date = models.DateField()
    due_date = models.DateField()
    original_value = models.DecimalField(decimal_places=2, max_digits=14)
    status = models.IntegerField(default=0, choices=STATUS_CHOICES)

    def __str__(self):
        return f'{self.payment_id}'
