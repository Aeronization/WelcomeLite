from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class JobOffer(models.Model):
    candidate_first_name = models.CharField(max_length=255, null=True)
    candidate_last_name = models.CharField(max_length=255, null=True)
    candidate_email_address = models.EmailField(max_length=128, null=True)
    start_date = models.DateTimeField(auto_now=False, null=True, blank=True)
    salary_offer = models.IntegerField(null=True, blank=True, default=0)
    offer_accepted = models.BooleanField(default=False, null=True, blank=True)

    job_poster = models.ForeignKey(User, null=True, blank=True, on_delete=models.SET_NULL)

    @classmethod
    def get_all_job_offers(cls, job_poster_id) -> list:
        """
        (R. Friel - October 12, 2020)
        Will return all of the job offers made by a job_poster.

        Args:
            job_poster_id (int): The primary key of the job_poster.

        Returns:
            list: A list of job offers made by the job_poster.
        """
        user = User.objects.get(pk=job_poster)
        job_offers: list = JobOffer.objects.filter(job_poster=user)
        return job_offers