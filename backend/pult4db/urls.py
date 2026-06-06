from django.urls import path

from .views import ListCompany, DetailCompany

urlpatterns = [
    path("company/", ListCompany.as_view(), name="company"),
    path("company/<str:company_id>/", DetailCompany.as_view(), name="detail_company"),
]
