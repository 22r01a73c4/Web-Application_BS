# main/models.py
from django.db import models

class IPO(models.Model):
    company_name = models.CharField(max_length=100)
    logo = models.ImageField(upload_to='images/')
    price_band = models.CharField(max_length=50)
    open_date = models.DateField(null=True, blank=True)
    close_date = models.DateField(null=True, blank=True)
    listing_date = models.DateField(null=True, blank=True)
    issue_size = models.CharField(max_length=50)
    issue_type = models.CharField(max_length=50)
    has_rhp = models.BooleanField(default=False)
    has_drhp = models.BooleanField(default=False)

    def __str__(self):
        return self.company_name
