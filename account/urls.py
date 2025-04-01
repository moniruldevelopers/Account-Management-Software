from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('upload-users/', upload_users, name='upload_users'),
    path('download-upload-format/', download_upload_format, name='download_upload_format'),
    path('', home, name='home'),
    path('transactions/', transaction_list, name='transaction_list'),
    path('add-transaction/', add_edit_transaction, name='add_transaction'),  # Used for both Add/Edit
    path('transaction-print/<int:transaction_id>/', transaction_print, name='transaction_print'),
    path('edit-transaction/<int:transaction_id>/', add_edit_transaction, name='edit_transaction'),
    path('transactions/delete/<int:transaction_id>/', delete_transaction, name='delete_transaction'),
    # user related url
    path('users/', user_list, name='user_list'),
    path('users/edit/<int:user_id>/', edit_user, name='edit_user'),
    path('users/delete/<int:user_id>/', delete_user, name='delete_user'),
    path('users/reset-password/<int:user_id>/', reset_password, name='reset_password'),
    # reports
    path('yearly-balance/', yearly_balance, name='yearly_balance'),
    path('yearly-given-borrow/', yearly_given_borrow, name='yearly_given_borrow'),   
    # category
    path('category-summary/', category_summary, name='category_summary'),
    path('category_transactions_filter/', category_transactions_filter, name='category_transactions_filter'),
    path('category_monthly_transactions/<str:category_name>/', category_monthly_transactions, name='category_monthly_transactions'),
    path('categories/', category_list, name='category_list'),   
    path('category/add/', add_or_edit_transaction_category, name='add_category'),
    path('category/edit/<int:category_id>/', add_or_edit_transaction_category, name='edit_category'),
    path('transactions-filter/', transaction_filter, name='transaction_filter'),
    path('user_profile/<str:username>/', user_profile, name='user_profile'),
    path('search-user/', search_user, name='search_user'),



]
