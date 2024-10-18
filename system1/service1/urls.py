from django.contrib import admin
from django.urls import path, include
from apps.core.views import UsersViewSet


urlpatterns = [
    path("admin/", admin.site.urls),
    path('users/<int:user_id>/', UsersViewSet.as_view()),
    path('users/', UsersViewSet.as_view()),
]
