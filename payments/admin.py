from django.contrib import admin

# Register your models here.
from payments.models import Supplier, Company, Payment


@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    list_display = [
        'company_name',
        'slug',
        'CNPJ',
    ]
    prepopulated_fields = {'slug': ('company_name',)}
    ordering = ('-slug',)


@admin.register(Supplier)
class SupplierAdmin(admin.ModelAdmin):
    list_display = [
        'supplier_name',
        'slug',
        'CNPJ',
    ]
    prepopulated_fields = {'slug': ('supplier_name',)}
    ordering = ('slug',)


@admin.register(Payment)
class PaymentAdmin(admin.ModelAdmin):
    list_display = [
        'payment_id',
        'company',
        'supplier',
        'issue_date',
        'due_date',
        'original_value',
        'status',
    ]
    ordering = ('-due_date', 'payment_id',)
    list_filter = ('company', 'supplier', 'status', )
