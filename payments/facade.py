from payments.models import Supplier, Company


def list_suppliers(company: Company):
    return list(company.objects.all())


def supplier_info(slug):
    return list(Supplier.objects.get(slug=slug))
