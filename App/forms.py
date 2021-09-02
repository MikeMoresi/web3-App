from django import forms
from .models import Transaction


class TransactionForm(forms.ModelForm):
    class Meta:
        model = Transaction
        fields = ['sender', 'recipient', 'amount']
        labels = {'sender': 'Sender Address', 'recipient': 'Recipient Address', 'amount': 'Amount'}