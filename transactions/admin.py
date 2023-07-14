from django.contrib import admin
from .models import Category,Transaction

class TransactionTabularInline(admin.TabularInline):
    model = Transaction
    extra = 3

class TransactionStackedInline(admin.StackedInline):
    model = Transaction
    extra = 2

class CategoryAdmin(admin.ModelAdmin):
    #Definiendo el orden de los campos al crear un registro nuevo
    fields = ['description','name']
    inlines=[TransactionTabularInline,TransactionStackedInline]
    list_display = ('name','description')
    search_fields = ['description']

class TransactionAdmin(admin.ModelAdmin):
    list_display = ('category','date','note','amount','type','is_recent_date_of_transaction')
    list_filter = ['date']
    search_fields = ['note']
    exclude= ['counter']

admin.site.register(Category,CategoryAdmin)
admin.site.register(Transaction,TransactionAdmin)

