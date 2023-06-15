from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("projects/", include('projects.urls')),
    path("", include('users.urls')),
    path("api/", include('api.urls')),
    # 1 - User submits email for reset
    path("reset_password/", auth_views.PasswordResetView.as_view(
        template_name="reset_password.html"), name="reset_password"),
    # 2 Email sent message
    path("reset_password_sent/", auth_views.PasswordResetDoneView.as_view(
        template_name="reset_password_sent.html"), name="password_reset_done"),
    # 3 Email with link and reset instructions
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(
        template_name="reset.html"), name="password_reset_confirm"),
    # 4 Password successfully reset message
    path("reset_password_complete/", auth_views.PasswordResetCompleteView.as_view(
        template_name="reset_password_complete.html"), name="password_reset_complete"),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
# This url is for production use
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
