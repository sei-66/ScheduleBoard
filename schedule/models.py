from django.db import models

# Create your models here.
class Company(models.Model):
    company_name = models.CharField(max_length=100)
    business = models.TextField(null=True, blank=True)
    memo = models.TextField(null=True, blank=True)
    hp_url = models.URLField(blank=True, null=True)
    rikunabi_url = models.URLField(blank=True, null=True)
    mainabi_url = models.URLField(blank=True, null=True)
    update_date = models.DateTimeField(auto_now=True)
    delete_date = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return self.company_name
