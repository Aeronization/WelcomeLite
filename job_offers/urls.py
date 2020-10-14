from django.urls import path

from job_offers.views import (
    JobOfferHome,
    JobOfferCreate,
    JobOfferRead,
    JobOfferUpdate,
    JobOfferDelete
)

app_name = "job_offers"

urlpatterns = [
    path("", JobOfferHome.as_view(), name="home"),
    path("create/", JobOfferCreate.as_view(), name="create"),
    path("read/<int:pk>/", JobOfferRead.as_view(), name="read"),
    path("update/<int:pk>/", JobOfferUpdate.as_view(), name="update"),
    path("delete/<int:pk>/", JobOfferDelete.as_view(), name="delete")
]