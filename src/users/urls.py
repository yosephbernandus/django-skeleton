from django.urls import path

from users import views

app_name = "users"

urlpatterns = [
    path("", views.index, name="index"),
    path("api/health", views.HealthCheckView.as_view(), name="health_check"),
    path("api/hello", views.HelloUserView.as_view(), name="hello_world"),
]
