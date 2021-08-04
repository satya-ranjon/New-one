from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from django.contrib.auth.views import PasswordResetView,PasswordResetDoneView,PasswordResetConfirmView,PasswordResetCompleteView
# app_name = 'Accound_app'

urlpatterns = [
    path("login_sign/", views.login_user, name="login"),
    path("sign_sign/", views.signup_user, name="signin"),
    path('activate/<uidb64>/<token>/', views.activate, name='activate'),
    path("log_out/", views.logout_user, name="logout"),
    path("change_password/", views.change_password, name="change_password"),

    path('password_reset/',auth_views.PasswordResetView.as_view(template_name='Accound_app/password_reset/password_reset.html'), name='password_reset'),

    path('password_reset_done/',auth_views.PasswordResetDoneView.as_view(template_name='Accound_app/password_reset/password_reset_done.html'), name='password_reset_done'),

    path('reset/<uidb64>/<token>/',auth_views.PasswordResetConfirmView.as_view(template_name='Accound_app/password_reset/password_reset_confirm.html'), name='password_reset_confirm'),

    path('password_reset_complete/',auth_views.PasswordResetCompleteView.as_view(template_name='Accound_app/password_reset/password_reset_complate.html'), name='password_reset_complete'),


]
