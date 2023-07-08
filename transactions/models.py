from django.db import models

class Category(models.Model):
    name = models.CharField('Category Name', max_length=50)
    description = models.CharField(max_length=250)

class TypeTransaction(models.IntegerChoices):
    EXPENSE = 0, 'Expense'
    REVENUE = 1, 'Revenue'

class Transaction(models.Model):
    category = models.ForeignKey('Category', on_delete=models.RESTRICT)
    date = models.DateField('date transaction')
    amount = models.DecimalField(max_digits=5,decimal_places=2)
    note = models.CharField(max_length=250)
    type = models.IntegerField(default=TypeTransaction.EXPENSE, choices=TypeTransaction.choices)


