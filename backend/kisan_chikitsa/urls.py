from django.contrib import admin
from django.urls import path, include, re_path
from django.shortcuts import render, redirect
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.views.generic import TemplateView
import os

def root_redirect(request):
    return render(request, 'index.html')

def redirect_to_signin(request):
    return redirect('accounts:signin')

def redirect_to_signup(request):
    return redirect('accounts:signup')

urlpatterns = [
    path("", root_redirect, name="root"),
    path("admin/", admin.site.urls),
    path("accounts/", include(("accounts.urls", "accounts"), namespace="accounts")),
    path("diagnose/", include("diagnosis.urls")),
    path("home/", include("home.urls")),
    # Legacy sign-in/sign-up paths redirect to the auth app
    re_path(r"^signin/?(?:\.html)?$", redirect_to_signin),
    re_path(r"^signup/?(?:\.html)?$", redirect_to_signup),
    # Frontend pages - handle both with and without trailing slashes
    re_path(r"^about/?(?:\.html)?$", TemplateView.as_view(template_name="about.html"), name="about"),
    re_path(r"^community/?(?:\.html)?$", TemplateView.as_view(template_name="community.html"), name="community"),
    re_path(r"^scheme/?(?:\.html)?$", TemplateView.as_view(template_name="scheme.html"), name="scheme"),
    re_path(r"^subscription/?(?:\.html)?$", TemplateView.as_view(template_name="subscription.html"), name="subscription"),
    re_path(r"^payment/?(?:\.html)?$", TemplateView.as_view(template_name="payment.html"), name="payment"),
    re_path(r"^diagnose/?(?:\.html)?$", TemplateView.as_view(template_name="diagnose.html"), name="diagnose_page"),
] + static(settings.STATIC_URL, document_root=settings.STATICFILES_DIRS[0]) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += staticfiles_urlpatterns()
