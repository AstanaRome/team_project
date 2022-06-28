from django import forms
from django.forms import ModelForm
from .models import Transfer


class TransferForm(ModelForm):
    wallet_from_id = forms.IntegerField(min_value=100000000, max_value=9999999999, label='С какого кошелька')
    wallet_to_id = forms.IntegerField(min_value=100000000, max_value=9999999999, label='На какой кошелек')

    class Meta:
        model = Transfer
        fields = ['wallet_from_id', 'wallet_to_id', 'note', 'money']
        labels = {
            'wallet_from_id': '',
            'wallet_to_id': '',
            'note': '',
            'money': ''
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for field in ['wallet_from_id', 'wallet_to_id', 'note', 'money']:
            self.fields[field].help_text = None
        self.fields['wallet_from_id'].widget = forms.NumberInput(attrs={'placeholder': 'Номер кошелька'})
        self.fields['wallet_to_id'].widget = forms.NumberInput(attrs={'placeholder': 'Номер кошелька'})
        self.fields['note'].widget = forms.Textarea(attrs={'placeholder': 'Заметка к переводу', 'rows': '5'})

