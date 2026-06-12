from django.urls import path

from .views import ListCompany, DetailCompany, ListGroupResponse, ListGroups

urlpatterns = [
    path("company/", ListCompany.as_view(), name="company"),
    path("company/groups/<str:company_id>/", ListGroups.as_view(), name="groups_company"),
    path("groupresponse/", ListGroupResponse.as_view(), name="group_response"),
    path("company/response-card/<str:company_id>/", DetailCompany.as_view(), name="detail_company"),
]
