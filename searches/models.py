from django.db import models


class ElasticSearch(models.Model):
    class Location(models.TextChoices):
        DEV = 'dev', 'dev'
        SERVICE = 'service', 'service'

    location = models.CharField(
        default=Location.DEV,
        choices=Location.choices,
        max_length=10
    )
    settings = models.TextField()
    mappings = models.TextField()
