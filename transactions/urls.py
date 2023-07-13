from django.urls import path
from . import views

app_name = "transactionsApp"
urlpatterns = [
    # * ex: /transactions/
    path('', views.index,name='index'),
    # * ex: /transactions/5
    path('<int:category_id>/', views.details,name='details'),
    # * ex: /transactions/details_category/5
    path('details_category/<int:category_id>/', views.details_category,name='details_category'),
     # * ex: /transactions/details_dates/transaction/5
    path('details_counter/transaction/<int:category_id>/', views.details_results_transaction,name='details_results_transaction')
]