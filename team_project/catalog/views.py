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
    # model = Transfer
    model = User


class IncomeView(LoginRequiredMixin, generic.ListView):# Income list for a specific user.
    # model = Income
    model = User


class ExpensesView(LoginRequiredMixin, generic.ListView):# Expenses list for a specific user.
    # model = Expense
    model = User



class UserListView(PermissionRequiredMixin, generic.ListView):
    permission_required = 'catalog.admin_required'
    model = User
    paginate_by = 10


class CurrencyDetailView(PermissionRequiredMixin, generic.DetailView):
    permission_required = 'catalog.admin_required'
    model = Currency

class CurrenciesListView(PermissionRequiredMixin, generic.ListView):
    permission_required = 'catalog.admin_required'
    model = Currency
    paginate_by = 10


class IncomeListView(PermissionRequiredMixin, generic.ListView):
    permission_required = 'catalog.admin_required'
    # model = Income
    model = User
    paginate_by = 10


class ExpensesListView(PermissionRequiredMixin, generic.ListView):
    permission_required = 'catalog.admin_required'
    # model = Expense
    model = User
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
    # model = Currency
    model = User


class CurrencyUpdate(PermissionRequiredMixin, UpdateView):
    permission_required = 'catalog.admin_required'
    # model = Currency
    model = User
    success_url = reverse_lazy('currencies')


class CurrencyDelete(PermissionRequiredMixin, DeleteView):
    permission_required = 'catalog.admin_required'
    # model = Currency
    model = User
    success_url = reverse_lazy('currencies')



class IncomeCreate(PermissionRequiredMixin, CreateView):
    permission_required = 'catalog.admin_required'
    # model = Income
    model = User


class IncomeUpdate(PermissionRequiredMixin, UpdateView):
    permission_required = 'catalog.admin_required'
    # model = Income
    model = User
    success_url = reverse_lazy('income')


class IncomeDelete(PermissionRequiredMixin, DeleteView):
    permission_required = 'catalog.admin_required'
    # model = Income
    model = User
    success_url = reverse_lazy('income')



class ExpenseCreate(PermissionRequiredMixin, CreateView):
    permission_required = 'catalog.admin_required'
    # model = Expense
    model = User


class ExpenseUpdate(PermissionRequiredMixin, UpdateView):
    permission_required = 'catalog.admin_required'
    # model = Expense
    model = User
    success_url = reverse_lazy('expenses')


class ExpenseDelete(PermissionRequiredMixin, DeleteView):
    permission_required = 'catalog.admin_required'
    # model = Expense
    model = User
    success_url = reverse_lazy('expenses')