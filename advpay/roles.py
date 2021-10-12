from rolepermissions.roles import AbstractUserRole

read_self_information = 'read_self_information'
request_payment_advance = 'request_payment_advance'


class Supplier(AbstractUserRole):
    available_permissions = {
        read_self_information: True,
        request_payment_advance: True,
    }


read_suppliers_information = 'read_suppliers_information'
read_company_information = 'read_company_information'
analyze_payment_advance = 'analyze_payment_advance'


class Company(AbstractUserRole):
    available_permissions = {
        read_suppliers_information: True,
        read_company_information: True,
        analyze_payment_advance: True,
    }
