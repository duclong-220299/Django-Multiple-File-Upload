from django.urls import path, include
from . import views

app_name = "website"

urlpatterns = [
    path("", views.UploadView.as_view(), name="index"),
    path("api/", include("website.api.urls")),
    path("download/<str:file_name>/", views.download, name="download"),
]
