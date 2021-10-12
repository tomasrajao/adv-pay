from django import forms

from .models import Payment


class PaymentForm(forms.ModelForm):
    class Meta:
        model = Payment
        fields = [
            'company',
            'supplier',
            'issue_date',
            'due_date',
            'original_value',
        ]
