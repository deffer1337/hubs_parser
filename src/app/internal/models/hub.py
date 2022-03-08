from django.db import models


class Hub(models.Model):
    """Hub model"""

    name = models.CharField(max_length=255)
    url = models.CharField(max_length=255)
    crawl_period = models.IntegerField(verbose_name="crawl_period_in_minutes")
