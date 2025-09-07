# from django.contrib import admin
# from django.urls import path, include
# from django.shortcuts import redirect

# def root_redirect(request):
#     return redirect("accounts:signin")  # ✅ correct (with namespace)

# urlpatterns = [
#     path("", root_redirect, name="root"),
#     path("admin/", admin.site.urls),
#     path("accounts/", include(("accounts.urls", "accounts"), namespace="accounts")),
#     path("diagnose/", include("diagnosis.urls")),

# ]
from django.contrib import admin
from django.urls import path, include
from django.shortcuts import redirect
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, re_path
from django.views.generic import TemplateView


def root_redirect(request):
    return redirect("accounts:signin")

urlpatterns = [
    path("", root_redirect, name="root"),
   
    path("admin/", admin.site.urls),
    path("home/", include('home.urls')),  # Include home app URLs
    path("", include('accounts.urls')),
    path("diagnose/", include("diagnosis.urls")),

        # frontend-only pages (static HTML)
    re_path(r"^$", TemplateView.as_view(template_name="frontend/index.html"), name="home"),
    re_path(r"^about/$", TemplateView.as_view(template_name="frontend/about.html"), name="about"),
    re_path(r"^community/$", TemplateView.as_view(template_name="frontend/community.html"), name="community"),
    re_path("scheme", TemplateView.as_view(template_name="frontend/scheme.html"), name="scheme"),
]


# ✅ Serve uploaded media files during development
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
