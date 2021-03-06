from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from django.urls import path, include
from . import views

urlpatterns = [
     #path('cuentas/login/', auth_views.login, name='login'),
     path('cuentas/login/', views.LoginView.as_view(), name='login'),
     path('cuentas/logout/', views.LogoutView.as_view(), name='logout'),
     path('cuentas/cambio-clave/', views.PasswordResetView.as_view(), name='password_reset'),
     path('cuentas/cambio-clave/finalizado', views.PasswordResetDoneView.as_view(), name='password_reset_done'),
     path('cuentas/<uidb64>/<token>/', views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
     path('cuentas/cambio-clave-completo/', views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
     path('registrar-organizador/', views.organizer_signup, name='organizer_signup'),
     path('activate/<uidb64>/<token>/',
        views.activate, name='activate'),

     path('', views.events_home, name='events_home'),
     
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
