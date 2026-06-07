from django.urls import path

from .views import ListCompany, DetailCompany, ListGroups

urlpatterns = [
    path("company/", ListCompany.as_view(), name="company"),
    path("company/groups/<str:company_id>/", ListGroups.as_view(), name="groups_company"),
    path("company/<str:company_id>/", DetailCompany.as_view(), name="detail_company"),
]
