from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic
from django.views.generic.edit import CreateView, DeleteView, UpdateView, FormMixin
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from .models import *
from .forms import TransferForm


def index(request):
    return render(request, 'catalog/index.html')


class UserDetailView(generic.DetailView):
    template_name = 'catalog/user_detail.html'
    model = User


class TransferListView(FormMixin, LoginRequiredMixin, generic.ListView):
    model = Transfer
    template_name = 'catalog/transfer_list.html'
    form_class = TransferForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        transfer_form = TransferForm()
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
        wallet_from_id = self.request.POST.get('wallet_from_id', '')
        wallet_to_id = self.request.POST.get('wallet_to_id', '')
        note = self.request.POST.get('note', '')
        money = self.request.POST.get('money', '')
        self.object.user = self.request.user
        self.object.wallet_from_id = wallet_from_id
        self.object.wallet_to_id = wallet_to_id
        self.object.note = note
        self.object.money = money
        self.object.save()
        return super().form_valid(form)

    def get_queryset(self):
        return Transfer.objects.filter(user=self.request.user)



class IncomeView(LoginRequiredMixin, generic.ListView):# Income list for a specific user.
    # model = Income
    model = User


class ExpensesView(LoginRequiredMixin, generic.ListView):# Expenses list for a specific user.
    # model = Expense
    model = User


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