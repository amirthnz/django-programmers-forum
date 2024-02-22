from django.urls import path, include
from django.contrib.auth import views as auth_views
from account import views
from account import forms

urlpatterns = [
    # registration with our method
    path('register/', views.register, name='register'),
    # Login using django classes
    path('login/', auth_views.LoginView.as_view(form_class = forms.LoginForm), name='login'),
    # Logout using django class
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    # Password reset using django classes
    path('password-reset/', auth_views.PasswordResetView.as_view(form_class = forms.PassResetForm),name='password_reset'),
    path('password-reset/done/', auth_views.PasswordResetDoneView.as_view(),name='password_reset_done'),
    path('password-reset-confirm/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(),name='password_reset_confirm'),
    path('password-reset-complete/',auth_views.PasswordResetCompleteView.as_view(),name='password_reset_complete'),

    # Dashboard
    path('', views.dashboard, name='dashboard'),
    # let the users to edit their profile
    path('edit/', views.edit, name='edit'),
]