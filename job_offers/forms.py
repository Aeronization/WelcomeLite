from django import forms

from .models import JobOffer

class JobOfferForm(forms.ModelForm):

    class Meta:
        model = JobOffer
        fields = [
            "candidate_first_name",
            "candidate_last_name",
            "candidate_email_address",
            "start_date",
            "salary_offer",
            "offer_accepted"
        ]
