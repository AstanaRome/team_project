from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from .models import Currency, Income, Transfer


def index(request):
    return render(request, 'catalog/index.html')


class UserDetailView(generic.DetailView):
    model = User


class TransferView(LoginRequiredMixin):
    model = Transfer
    model = User


class IncomeListView(LoginRequiredMixin, generic.ListView):# Income list for a specific user.
    model = Income
    paginate_by = 10


class ExpenditureListView(LoginRequiredMixin, generic.ListView):# Expenses list for a specific user.
    model = Expenditure
    paginate_by = 10



class UserListView(PermissionRequiredMixin, generic.ListView):
    permission_required = 'catalog.admin_required'
    model = User
    template_name = 'catalog/user_list.html'
    paginate_by = 10


class CurrencyDetailView(PermissionRequiredMixin, generic.DetailView):
    permission_required = 'catalog.admin_required'
    model = Currency

class CurrenciesListView(PermissionRequiredMixin, generic.ListView):
    permission_required = 'catalog.admin_required'
    model = Currency
    paginate_by = 10


class ExchangeRateListView(LoginRequiredMixin, generic.ListView):
    model = ExchangeRate
    paginate_by = 10


class IncomeCategoryListView(PermissionRequiredMixin, generic.ListView):
    permission_required = 'catalog.admin_required'
    model = IncomeCategory
    paginate_by = 10


class ExpenseCategoryListView(PermissionRequiredMixin, generic.ListView):
    permission_required = 'catalog.admin_required'
    model = ExpenseCategory
    paginate_by = 10


class WalletListView(LoginRequiredMixin, generic.ListView):# Wallets list for a specific user.
    model = Wallet
    paginate_by = 10



class UserCreate(PermissionRequiredMixin, CreateView):
    permission_required = 'catalog.admin_required'
    model = User

class UserUpdate(PermissionRequiredMixin, UpdateView):
    permission_required = 'catalog.admin_required'
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



class ExchangeRateCreate(PermissionRequiredMixin, CreateView):
    permission_required = 'catalog.admin_required'
    model = ExchangeRate

class ExchangeRateUpdate(PermissionRequiredMixin, UpdateView):
    permission_required = 'catalog.admin_required'
    model = ExchangeRate
    success_url = reverse_lazy('rates')

class ExchangeRateDelete(PermissionRequiredMixin, DeleteView):
    permission_required = 'catalog.admin_required'
    model = ExchangeRate
    success_url = reverse_lazy('rates')



class IncomeCategoryCreate(PermissionRequiredMixin, CreateView):
    permission_required = 'catalog.admin_required'
    model = IncomeCategory

class IncomeCategoryUpdate(PermissionRequiredMixin, UpdateView):
    permission_required = 'catalog.admin_required'
    model = IncomeCategory
    success_url = reverse_lazy('income-cats')

class IncomeCategoryDelete(PermissionRequiredMixin, DeleteView):
    permission_required = 'catalog.admin_required'
    model = IncomeCategory
    success_url = reverse_lazy('income-cats')



class IncomeCreate(LoginRequiredMixin, CreateView):
    model = Income
    model = User

class IncomeUpdate(LoginRequiredMixin, UpdateView):
    model = Income
    success_url = reverse_lazy('income')

class IncomeDelete(LoginRequiredMixin, DeleteView):
    model = Income
    success_url = reverse_lazy('income')



class ExpenseCategoryCreate(PermissionRequiredMixin, CreateView):
    permission_required = 'catalog.admin_required'
    model = ExpenseCategory

class ExpenseCategoryUpdate(PermissionRequiredMixin, UpdateView):
    permission_required = 'catalog.admin_required'
    model = ExpenseCategory
    success_url = reverse_lazy('expenses')

class ExpenseCategoryDelete(PermissionRequiredMixin, DeleteView):
    permission_required = 'catalog.admin_required'
    model = ExpenseCategory
    success_url = reverse_lazy('expenses')



class ExpenditureCreate(LoginRequiredMixin, CreateView):
    model = Expenditure
    model = User

class ExpenditureUpdate(LoginRequiredMixin, UpdateView):
    model = Expenditure
    success_url = reverse_lazy('expenditures')

class ExpenditureDelete(LoginRequiredMixin, DeleteView):
    model = Expenditure
    success_url = reverse_lazy('expenditures')



class WalletCreate(LoginRequiredMixin, CreateView):
    model = Wallet
    model = User

class WalletUpdate(LoginRequiredMixin, UpdateView):
    model = Wallet
    success_url = reverse_lazy('wallets')

class WalletDelete(LoginRequiredMixin, DeleteView):
    model = Wallet
    success_url = reverse_lazy('wallets')