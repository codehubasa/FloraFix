from django.urls import path
from . import views

urlpatterns = [
    path('', views.index_view, name='home'),
]
# urlpatterns = [
#     path('scheme/', views.scheme_view, name='scheme'),  # ✅ This matches {% url 'scheme' %}
# ]
