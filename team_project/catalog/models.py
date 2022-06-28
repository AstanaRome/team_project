import datetime
from django.contrib.auth.models import User
from django.db import models


# Курс валют
class ExchangeRate(models.Model):
    name = models.CharField(max_length=20)
    rate = models.DecimalField(max_digits=12, decimal_places=4)

    def __str__(self):
        return self.name


# Валюта
class Currency(models.Model):
    name = models.CharField(max_length=20, help_text='Enter the currency name')
    exchange_rate = models.ManyToManyField(ExchangeRate)

    def __str__(self):
        return self.name


#Категория затрат
class ExpenseCategory(models.Model):
    name = models.CharField(max_length=150)

    def __str__(self):
        return self.name


class IncomeCategory(models.Model):
    name = models.CharField(max_length=150)

    def __str__(self):
        return self.name


# Кошелек пользователя
class Wallet(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='user_wallets') #владелец кошелька
    unique_num = models.PositiveBigIntegerField() #уникальный номер кошелька
    currency = models.ForeignKey(Currency, on_delete=models.SET_NULL, null=True) #валюта кошелька
    money = models.DecimalField(max_digits=12, decimal_places=4) #кол-во денег в кошельке
    main_wallet = models.BooleanField(default=False) #кошелек основной или нет

    def __str__(self):
        return f'{self.currency}'


# Расходы
class Expenditure(models.Model):
    wallet = models.ForeignKey(Wallet, on_delete=models.SET_NULL, null=True) #Кошелек с которого была сделана оплата
    category = models.ForeignKey(ExpenseCategory, on_delete=models.SET_NULL, null=True) #Системой выберается категория затраты
    date = models.DateTimeField(default=datetime.datetime.now()) #Автоматически вводит текущую дату при создании записи в таблице
    note = models.CharField(max_length=100, blank=True, null=True) #Пользователем в ручную вводится заметка
    money = models.DecimalField(max_digits=12, decimal_places=4) #Системой вводится кол-во затраченных денег

    def __str__(self):
        return f'{self.wallet}'

    class Meta:
        ordering = ['-id']


# Доходы
class Income(models.Model):
    wallet = models.ForeignKey(Wallet, on_delete=models.SET_NULL, null=True) #Кошелек на который поступили деньги
    category = models.ForeignKey(IncomeCategory, on_delete=models.SET_NULL, null=True) #Системой выберается категория дохода
    date = models.DateTimeField(default=datetime.datetime.now()) #Автоматически вводит текущую дату при создании записи в таблице
    note = models.CharField(max_length=100, blank=True, null=True) #Пользователем в ручную вводится заметка
    money = models.DecimalField(max_digits=12, decimal_places=4) #Системой вводится кол-во полученных денег

    def __str__(self):
        return f'{self.wallet}'

    class Meta:
        ordering = ['-id']


#Переводы
class Transfer(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    wallet_from_id = models.IntegerField() #Id кошелька с которого был сделан перевод
    wallet_to_id = models.IntegerField() #Id кошелька на который был сделан перевод
    date = models.DateTimeField(default=datetime.datetime.now()) #Дата перевода(ставится автоматический дата при создании записи в таблице)
    note = models.CharField(max_length=100) #Заметки к переводу
    money = models.DecimalField(max_digits=8, decimal_places=2) #Сумма переведенных денег

    wallet_choices = (
        ('Wallet')
    )

    def __str__(self):
        return f'{self.user}'

    class Meta:
        ordering = ['-id']








