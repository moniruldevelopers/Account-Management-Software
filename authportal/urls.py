from django.urls import path
from .views import *
from django.contrib.auth.views import PasswordResetView,PasswordResetDoneView,PasswordResetConfirmView,PasswordResetCompleteView
urlpatterns = [

    path('login/',loginuser, name='login'),
    path('logout/',logoutuser, name='logout'),
    path('change_password/',change_password, name='change_password'),
    # path('signup/',register, name='add_student'),
    # path('confirm_email/',confirm_email, name='confirm_email'),
    # path('activate/<uidb64>/<token>/', activate, name='activate'),
    # path('reset/password/',PasswordResetView.as_view(template_name='authportal/reset_password.html'), name='password_reset'),

    # path('reset/password/done/',PasswordResetDoneView.as_view(template_name='authportal/reset_password_done.html'), name='password_reset_done'),

    # path('reset/<uidb64>/<token>/',PasswordResetConfirmView.as_view(template_name='authportal/password_reset_confirm.html'), name='password_reset_confirm'),

    # path('reset/done',PasswordResetCompleteView.as_view(template_name='authportal/password_reset_complete_done.html'), name='password_reset_complete'),

    # path('staff-superusers/', staff_superusers_view, name='staff_superusers'),



]