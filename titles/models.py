from django.db import models

from authentication.models import User
from utils.uuid import ID_LENGTH, generate_uuid


class Title(models.Model):
    id = models.CharField(
        max_length=ID_LENGTH, primary_key=True,
        default=generate_uuid, editable=False
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    proprietor = models.CharField(max_length=255)
    tenure = models.CharField(max_length=255)
    tenure_volume = models.CharField(max_length=255)
    tenure_folio_no = models.CharField(max_length=255)
    size_of_land = models.CharField(max_length=255)
    lease_period = models.CharField(max_length=255)
    lease_authority = models.CharField(max_length=255)
    district = models.CharField(max_length=255)
    parish = models.CharField(max_length=255)
    block = models.CharField(max_length=255)
    plot = models.CharField(max_length=255)
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)

    class Meta:
        unique_together = (("district", "parish", "block", "plot"))

    def __str__(self):
        return f"Title id: {self.id}"
