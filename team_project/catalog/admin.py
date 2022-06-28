from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(ExchangeRate)
admin.site.register(Currency)
admin.site.register(ExpenseCategory)
admin.site.register(IncomeCategory)
admin.site.register(Wallet)
admin.site.register(Expenditure)
admin.site.register(Transfer)
admin.site.register(Income)