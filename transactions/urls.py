from django.urls import path
from . import views

app_name = "transactionsApp"
urlpatterns = [
    # * ex: /transactions/
    path('', views.IndexView.as_view(),name='index'),
    # * ex: /transactions/5
    path('<int:category_id>/', views.details,name='details'),
    # * ex: /transactions/details_category/5
    path('details_category/<slug:slug>/', views.DetailsCategoryView.as_view(),name='details_category'),
     # * ex: /transactions/details_consult_transaction/5
    path('details_consult_transaction/<int:category_id>/', views.details_consult_transaction,name='details_consult_transaction'),
     # * ex: /transactions/details_results_category/5
    path('details_results_category/<slug:slug>/', views.DetailsResultsCategoryView.as_view(),name='details_results_category'),
]