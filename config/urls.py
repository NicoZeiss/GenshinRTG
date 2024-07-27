from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin-panel/', admin.site.urls),
    path('', include('genshin_app.urls')),

    path("__reload__/", include("django_browser_reload.urls")),
]
