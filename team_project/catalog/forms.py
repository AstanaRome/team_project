from django import forms
from django.contrib.auth.models import User
from django.forms import ModelForm
from .models import Transfer, Wallet


class TransferForm(ModelForm):
    class Meta:
        model = Transfer
        fields = ['wallet_from', 'wallet_to', 'note', 'money']
        labels = {
            'wallet_from': '',
            'wallet_to': '',
            'note': '',
            'money': ''
        }

    def __init__(self, current_user, *args, **kwargs):
        super(TransferForm, self).__init__(*args, **kwargs)
        self.fields['user'].queryset = self.fields['user'].queryset.exclude(id=current_user.id)

        for field in ['wallet_from', 'wallet_to', 'note', 'money']:
            self.fields[field].help_text = None
        self.fields['note'].widget = forms.Textarea(attrs={'placeholder': 'Заметка к переводу', 'rows': '5'})


class UserForm(ModelForm):
    password = forms.CharField(label='Пароль', widget=forms.PasswordInput)
    confirm_password = forms.CharField(label='Повторите пароль', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email']
        labels = {
            'username': 'Логин',
            'first_name': 'Имя',
            'last_name': 'Фамилия',
            'email': 'Почта',
        }

    def clean_pass(self):
        cd = self.cleaned_data
        if cd['password'] != cd['confirm_password']:
            raise forms.ValidationError('Пароли не совпадают')
        return cd['confirm_password']


class WalletCreateForm(ModelForm):
    class Meta:
        model = Wallet
        fields = ['currency']
        labels = {
            'currency': 'Выберите валюту кошелька'
        }

