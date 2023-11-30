import uuid
from django.db import models

# Create your models here.
from django.db import models


class FoodTruck(models.Model):
    """
    FoodTruck model.
    """

    id = models.UUIDField(
        verbose_name=("Id"),
        primary_key=True,
        default=uuid.uuid4,
        editable=False,
        unique=True,
    )
    location_id = models.CharField(max_length=100)
    applicant = models.CharField(max_length=200)
    facility_type = models.CharField(max_length=100)
    location_description = models.CharField(max_length=300)
    address = models.CharField(max_length=200)
    blocklot = models.CharField(max_length=100)
    block = models.CharField(max_length=50)
    lot = models.CharField(max_length=50)
    food_items = models.TextField()
    latitude = models.FloatField()
    longitude = models.FloatField()
    zip_codes = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return str(self.applicant)
