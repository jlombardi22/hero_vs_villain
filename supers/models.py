from django.db import models
from super_type.models import SuperType
# Create your models here.


class Supers(models.Model):
    name = models.CharField(max_length=255, null=True)
    alter_ego = models.CharField(max_length=255, null=True)
    primary_ability = models.CharField(max_length=255, null=True)
    secondary_ability = models.CharField(max_length=255, null=True)
    catchphrase = models.CharField(max_length=255, null=True)
    super_type = models.ForeignKey(
        SuperType, on_delete=models.CASCADE, null=True)

    # super_type = models.ForeignKey(
    #   SuperType, on_delete=models.CASCADE, null=True)
