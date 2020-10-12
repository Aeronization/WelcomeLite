from django import forms

from .models import JobOffer

class JobOfferForm(forms.ModelForm):

    class Meta:
        model = JobOffer
        fields = '__all__'
