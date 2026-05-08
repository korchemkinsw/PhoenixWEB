from django.urls import path

from .views import ListCompany

urlpatterns = [
    path("company", ListCompany.as_view(), name="company"),
]
