from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('user/<int:pk>', views.UserDetailView.as_view(), name='user'),
    path('transfer/', views.TransferView, name='transfer'),
    path('my-income/', views.IncomeListView.as_view(), name='my-income'),
    path('my-expenses/', views.ExpenditureListView.as_view(), name='my-expenses'),

    path('users/', views.UserListView.as_view(), name='users'),
    path('currencies/', views.CurrencyListView.as_view(), name='currencies'),
    path('income-cats/', views.IncomeCategoryListView.as_view(), name='income-cats'),
    path('expenses-cats/', views.ExpenseCategoryListView.as_view(), name='expenses-cats'),
    path('wallets/', views.WalletListView.as_view(), name='wallets'),
    path('rates/', views.ExchangeRateListView.as_view(), name='rates'),

    path('user/create/', views.UserCreate.as_view(), name='user-create'),
    path('user/<int:pk>/update/', views.UserUpdate.as_view(), name='user-update'),
    path('user/<int:pk>/delete/', views.UserDelete.as_view(), name='user-delete'),

    path('currency/create/', views.CurrencyCreate.as_view(), name='currency-create'),
    path('currency/<int:pk>/update/', views.CurrencyUpdate.as_view(), name='currency-update'),
    path('currency/<int:pk>/delete/', views.CurrencyDelete.as_view(), name='currency-delete'),

    path('rate/create/', views.ExchangeRateCreate.as_view(), name='rate-create'),
    path('rate/<int:pk>/update/', views.ExchangeRateUpdate.as_view(), name='rate-update'),
    path('rate/<int:pk>/delete', views.ExchangeRateDelete.as_view(), name='rate-delete'),

    path('expenditure/create/', views.ExpenditureCreate.as_view(), name='expenditure-create'),
    path('expenditure/<int:pk>/update/', views.ExpenditureUpdate.as_view(), name='expenditure-update'),
    path('expenditure/<int:pk>/delete/', views.ExpenditureDelete.as_view(), name='expenditure-delete'),

    path('income/create/', views.IncomeCreate.as_view(), name='income-create'),
    path('income/<int:pk>/update/', views.IncomeUpdate.as_view(), name='income-update'),
    path('income/<int:pk>/delete/', views.IncomeDelete.as_view(), name='income-delete'),

    path('expense/create/', views.ExpenseCategoryCreate.as_view(), name='expense-create'),
    path('expense/<int:pk>/update/', views.ExpenseCategoryUpdate.as_view(), name='expense-update'),
    path('expense/<int:pk>/delete/', views.ExpenseCategoryDelete.as_view(), name='expense-delete'),

    path('income-cats/create/', views.IncomeCategoryCreate.as_view(), name='income-cat-create'),
    path('income-cats/<int:pk>/update/', views.IncomeCategoryUpdate.as_view(), name='income-cat-update'),
    path('income-cats/<int:pk>/delete/', views.IncomeCategoryDelete.as_view(), name='income-cat-delete'),

    path('wallet/create/', views.WalletCreate.as_view(), name='wallet-create'),
    path('wallet/<int:pk>/update/', views.WalletUpdate.as_view(), name='wallet-update'),
    path('wallet/<int:pk>/delete/', views.WalletDelete.as_view(), name='wallet-delete'),
]