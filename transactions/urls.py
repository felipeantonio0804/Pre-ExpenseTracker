from django.urls import path
from . import views

app_name = "transactionsApp"
urlpatterns = [
    # * ex: /transactions/
    path('', views.index,name='index'),
    # * ex: /transactions/5
    path('<int:category_id>/usodetag/url/con_app_name_view_name/', views.details,name='details'),
    # * ex: /transactions/details_dates/5
    path('details_dates/<int:category_id>/', views.details_dates,name='details_dates')
]