from django.urls import path, include
from django.views.generic import RedirectView
from django.contrib.auth import views as auth_views

from dashboard import views


urlpatterns = [
    path('', RedirectView.as_view(url='login', permanent=False), name='index'),
    path('dashboard/', include('dashboard.urls'), name='dashboard'),
    path('api/', include('core.urls'), name='api'),
    path('application/', views.ApplicationView.as_view(),
         name='application'),
    path('login', auth_views.LoginView.as_view(template_name="authentication/login.html",
                                               success_url="/dashboard",
                                               redirect_authenticated_user=True), name='login'),
    path('logout/', auth_views.LogoutView.as_view(),
         name='logout'),
    path('password_reset/', auth_views.PasswordResetView.as_view(template_name="authentication/reset.html",
                                                                email_template_name="email/reset.html",
                                                                success_url="home:password_reset_done",
                                                                ),
         name='password_reset'),
    path('password_change/', auth_views.PasswordChangeView.as_view(template_name="authentication/password.html"),
         name="password_change"),
    path('password_reset_done/', auth_views.PasswordResetDoneView.as_view(), name="password_reset_done"),
    path('password_reset_confirm/<str:uidb64>/<str:token>/', auth_views.PasswordResetConfirmView.as_view(),
         name="password_reset_confirm"),
]
