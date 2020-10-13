from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.contrib import messages

# (R. Friel - October 12, 2020) - Import CRUD views.
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.views.generic import ListView
from django.views.generic.detail import DetailView

from .models import JobOffer
from .forms import JobOfferForm


class JobOfferHome(LoginRequiredMixin, SuccessMessageMixin, ListView):
    template_name = "job_offers/home.html"
    model = JobOffer

    def get_queryset(self):
        queryset = super(JobOfferHome, self).get_queryset()
        return queryset.filter(job_poster=self.request.user)

class JobOfferCreate(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    template_name = "job_offers/create.html"
    form_class = JobOfferForm
    model = JobOffer
    success_url = reverse_lazy("job_offers:home")
    success_message = "Your job offer has been successfully created."

    def form_valid(self, form, *args, **kwargs):
        form.instance.job_poster = self.request.user
        return super().form_valid(form)

class JobOfferRead(LoginRequiredMixin, SuccessMessageMixin, DetailView):
    template_name = "job_offers/detail.html"
    model = JobOffer
    form_class = JobOfferForm


class JobOfferUpdate(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    template_name = "job_offers/update.html"
    form_class = JobOfferForm
    model = JobOffer
    success_url = reverse_lazy("job_offers:home")
    success_message = "Your updates have been saved."


class JobOfferDelete(LoginRequiredMixin, SuccessMessageMixin, DeleteView):
    template_name = "job_offers/delete.html"
    model = JobOffer
    success_url = reverse_lazy("job_offers:home")
    success_message = "Your selected job offer has been deleted."

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, self.success_message)
        return super(JobOfferDelete, self).delete(request, *args, **kwargs)