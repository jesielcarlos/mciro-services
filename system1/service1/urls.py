from django.contrib import admin
from django.urls import path, include
from apps.core.views import UserView


urlpatterns = [
    path("admin/", admin.site.urls),
    path('users/<int:user_id>/', UserView.as_view()),
    path('users/', UserView.as_view()),
]
