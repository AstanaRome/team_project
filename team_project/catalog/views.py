from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic
from django.views.generic.edit import CreateView, DeleteView, UpdateView, FormMixin
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from .models import *
from .forms import TransferForm, UserForm, WalletCreateForm
import random


def index(request):
    wallet_form = WalletCreateForm()
    return render(request, 'catalog/index.html', {'wallet_form': wallet_form})


class UserDetailView(generic.DetailView):
    template_name = 'catalog/user_detail.html'
    model = User


class TransferListView(FormMixin, LoginRequiredMixin, generic.ListView):
    model = Transfer
    template_name = 'catalog/transfer_list.html'
    form_class = TransferForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs).__init__(self)
        transfer_form = TransferForm(current_user=self.request.user)
        context['transfer_form'] = transfer_form
        return context

    def get_success_url(self):
        return reverse_lazy('transfer')

    def post(self, request, *args, **kwargs):
        transfer_form = TransferForm(request.POST, None)
        if transfer_form.is_valid():
            return self.transfer_form_valid(transfer_form)
        else:
            return self.form_invalid(transfer_form)

    def transfer_form_valid(self, form):
        self.object = form.save(commit=False)
        wallet_from = self.request.POST.get('wallet_from', '')
        wallet_to = self.request.POST.get('wallet_to', '')
        note = self.request.POST.get('note', '')
        money = self.request.POST.get('money', '')
        self.object.user = self.request.user
        self.object.wallet_from = wallet_from
        self.object.wallet_to = wallet_to
        self.object.note = note
        self.object.money = money
        self.object.save()
        return super().form_valid(form)

    def get_queryset(self):
        return Transfer.objects.filter(user=self.request.user)


class IncomeView(LoginRequiredMixin, generic.ListView):# Income list for a specific user.
    model = Income


class ExpensesView(LoginRequiredMixin, generic.ListView):# Expenses list for a specific user.
    model = Expenditure
    template_name = 'catalog/expense_list.html'


class UserListView(PermissionRequiredMixin, generic.ListView):
    permission_required = 'catalog.admin_required'
    template_name = 'catalog/user_list.html'
    model = User
    paginate_by = 10


class CurrenciesListView(PermissionRequiredMixin, generic.ListView):
    permission_required = 'catalog.admin_required'
    template_name = 'catalog/currency_list.html'
    model = Currency
    paginate_by = 10


class IncomeListView(PermissionRequiredMixin, generic.ListView):
    permission_required = 'catalog.admin_required'
    model = Income
    paginate_by = 10


class ExpensesListView(PermissionRequiredMixin, generic.ListView):
    permission_required = 'catalog.admin_required'
    model = Expenditure
    paginate_by = 10


class UserCreate(CreateView):
    form_class = UserForm
    model = User
    success_url = reverse_lazy('index')

    def post(self, request, *args, **kwargs):
        user_form = UserForm(request.POST)
        if user_form.is_valid():
            new_user = user_form.save(commit=False)
            new_user.set_password(user_form.cleaned_data['password'])
            new_user.save()
            return super().form_valid(user_form)
        else:
            return self.form_invalid(user_form)


class UserUpdate(PermissionRequiredMixin, UpdateView):
    permission_required = 'catalog.admin_required'
    fields = '__all__'
    model = User
    success_url = reverse_lazy('users')


class UserDelete(PermissionRequiredMixin, DeleteView):
    permission_required = 'catalog.admin_required'
    model = User
    success_url = reverse_lazy('users')


class CurrencyCreate(PermissionRequiredMixin, CreateView):
    permission_required = 'catalog.admin_required'
    model = Currency


class CurrencyUpdate(PermissionRequiredMixin, UpdateView):
    permission_required = 'catalog.admin_required'
    model = Currency
    success_url = reverse_lazy('currencies')


class CurrencyDelete(PermissionRequiredMixin, DeleteView):
    permission_required = 'catalog.admin_required'
    model = Currency
    success_url = reverse_lazy('currencies')


class IncomeCreate(PermissionRequiredMixin, CreateView):
    permission_required = 'catalog.admin_required'
    model = Income


class IncomeUpdate(PermissionRequiredMixin, UpdateView):
    permission_required = 'catalog.admin_required'
    model = Income
    success_url = reverse_lazy('income')


class IncomeDelete(PermissionRequiredMixin, DeleteView):
    permission_required = 'catalog.admin_required'
    model = Income
    success_url = reverse_lazy('income')



class ExpenseCreate(PermissionRequiredMixin, CreateView):
    permission_required = 'catalog.admin_required'
    model = Expenditure
    model = User


class ExpenseUpdate(PermissionRequiredMixin, UpdateView):
    permission_required = 'catalog.admin_required'
    model = Expenditure
    success_url = reverse_lazy('expenses')


class ExpenseDelete(PermissionRequiredMixin, DeleteView):
    permission_required = 'catalog.admin_required'
    model = Expenditure
    success_url = reverse_lazy('expenses')


class ExchangeRateUpdate(UpdateView):
    model = ExchangeRate
    template_name = 'catalog/exchange_rate_form.html'
    fields = '__all__'
    success_url = reverse_lazy('currencies')


class CreateWallet(CreateView):
    model = Wallet
    form_class = WalletCreateForm

    def get_success_url(self):
        return reverse_lazy('index')

    def post(self, request, *args, **kwargs):
        wallet_form = WalletCreateForm(request.POST)
        if wallet_form.is_valid():
            return self.wallet_form_valid(wallet_form)
        else:
            return self.form_invalid(wallet_form)

    def wallet_form_valid(self, form):
        new_wallet = form.save(commit=False)
        money = random.randint(500, 100000)
        new_wallet.user = self.request.user
        new_wallet.money = money
        new_wallet.save()
        return super().form_valid(form)



