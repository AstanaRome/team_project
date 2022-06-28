from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('user/<int:pk>', views.UserDetailView.as_view(), name='user'),
    path('transfer/', views.TransferView, name='transfer'),
    path('my-income/', views.IncomeView.as_view(), name='my-income'),
    path('my-expenses/', views.ExpensesView.as_view(), name='my-expenses'),

    path('users/', views.UserListView.as_view(), name='users'),
    path('currencies/', views.CurrenciesListView.as_view(), name='currencies'),
    path('income/', views.IncomeListView.as_view(), name='income'),
    path('expenses/', views.ExpensesListView.as_view(), name='expenses'),

    path('user/create/', views.UserCreate.as_view(), name='user-create'),
    path('user/<int:pk>/update/', views.UserUpdate.as_view(), name='user-update'),
    path('user/<int:pk>/delete/', views.UserDelete.as_view(), name='user-delete'),

    path('currency/<int:pk>/', views.CurrencyDetailView.as_view(), name='currency-detail'),
    path('currency/create/', views.CurrencyCreate.as_view(), name='currency-create'),
    path('currency/<int:pk>/update/', views.CurrencyUpdate.as_view(), name='currency-update'),
    path('currency/<int:pk>/delete/', views.CurrencyDelete.as_view(), name='currency-delete'),

    path('income/create/', views.IncomeCreate.as_view(), name='income-create'),
    path('income/<int:pk>/update/', views.IncomeUpdate.as_view(), name='income-update'),
    path('income/<int:pk>/delete/', views.IncomeDelete.as_view(), name='income-delete'),

    path('expense/create/', views.ExpenseCreate.as_view(), name='expense-create'),
    path('expense/<int:pk>/update/', views.ExpenseUpdate.as_view(), name='expense-update'),
    path('expense/<int:pk>/delete/', views.ExpenseDelete.as_view(), name='expense-delete'),
]