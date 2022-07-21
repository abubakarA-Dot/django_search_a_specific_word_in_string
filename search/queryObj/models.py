import uuid
from django.db import models
from django.urls import reverse
# from accounts.models import FarmOwnerUser
from tinymce import models as tinymce_models



# Create your models here.
class Farm(models.Model):
    id = models.UUIDField(
    primary_key = True,
    default=uuid.uuid4,
    editable=False)
    farm_name = models.CharField(max_length=200)
    # owner = models.ForeignKey(
    # FarmOwnerUser,
    # on_delete=models.SET_NULL,
    # null = True,
    # blank = True,
    # )
    # associated_group = models.CharField(max_length=200)
    # consultants = models.ManyToManyField(Consultant)
    class Meta:
        permissions = [
        ('special_status', 'Can view farms')
        ]



    def __str__(self):
        return self.farm_name



    def get_absolute_url(self):
        return reverse("farm_detail", args=[str(self.id)])

class Report(models.Model):
    id = models.UUIDField(
    primary_key = True,
    default=uuid.uuid4,
    editable=False)
    title = models.CharField(max_length=200)
    # author = models.ForeignKey(ReportAuthor, on_delete=models.PROTECT,blank=True,
    # null=True)
    farm = models.ForeignKey(Farm, on_delete=models.SET_NULL, null=True)
    checks_ran = tinymce_models.HTMLField(blank=True, null=True)
    recommendations = tinymce_models.HTMLField(blank=True, null=True)

    def __str__(self):
        return str(self.title)