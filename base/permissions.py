from rolepermissions.permissions import register_object_checker

from advpay.roles import Supplier, Company


@register_object_checker()
def company_content(role, user, supplier):
    if role == Company:
        return True
    return False


@register_object_checker()
def supplier_content(role, user, supplier):
    if role == Supplier:
        return True
    return False
