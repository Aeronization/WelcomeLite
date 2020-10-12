from django.db import models

# Create your models here.
class JobOffer(models.Model):
    candidate_first_name = models.CharField(max_length=255)
    candidate_last_name = models.CharField(max_length=255)
    candidate_email_address = models.EmailField(max_length=128, null=True)