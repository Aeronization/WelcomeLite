from django.urls import path

from job_offers.views import (
    JobOfferHomeView,
    JobOfferCreate,
    JobOfferRead,
    JobOfferUpdate,
    JobOfferDelete
)

urlpatterns = [
    path("", JobOfferHomeView.as_view(), name="home"),
    path("create/", JobOfferCreate.as_view(), name="create"),
    path("read/", JobOfferRead.as_view(), name="read"),
    path("update/", JobOfferUpdate.as_view(), name="update"),
    path("delete/", JobOfferDelete.as_view(), name="delete")
]