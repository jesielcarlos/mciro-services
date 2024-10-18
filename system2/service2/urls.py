from django.contrib import admin
from django.urls import path, include
from apps.core.views import OrderView


urlpatterns = [
    path("admin/", admin.site.urls),
    path('orders/', OrderView.as_view()),
]
