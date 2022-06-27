from django.contrib import admin
from .models import *

admin.site.register(ExchangeRate)
admin.site.register(Currency)
admin.site.register(ExpenseCategory)
admin.site.register(IncomeCategory)
admin.site.register(Expenditure)
admin.site.register(Income)
admin.site.register(Wallet)
admin.site.register(Transfer)
