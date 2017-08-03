from django.db import models

from django.contrib.auth.models import AbstractUser
from django.utils.translation import ugettext_lazy as _
from model_utils.models import TimeStampedModel
# from django_dropbox import storage
from model_utils import models as ms


class User(AbstractUser):
    """
    User Model
    """
    # title = models.CharField(_('title of User'), blank=True, max_length=255)
    phone_number = models.CharField(max_length=30, null=True)
    address = models.TextField(null=True)


    def __str__(self):
        return self.username


class Document(models.Model):
    """
    A Document represents a booking to be printed.
    """
    title = models.CharField(max_length=256, null=True)
    file = models.FileField(null=True)
    brief = models.TextField(null=True)

    def __str__(self):
        return self.title


class PrintJob(TimeStampedModel):
    """
    Print Jobs sent into the organisation
    """
    charged_to = models.ForeignKey(User)
    printer = models.CharField(max_length=256)
    copies = models.IntegerField()
    cost = models.IntegerField()
    status_choices = (("Started", "Started"), ("Pending",
                                               "Pending"), ("Completed", "Completed"), ("Paid", "Paid"))

    status = models.CharField(choices=status_choices, max_length=256)
    document = models.ForeignKey(Document)

    def __str__(self):
        return self.charged_to.username + " - " + self.document.title


class PricingManager(models.Manager):
    pass


class Pricing(models.Model):
    """
    Enables admin to change and edit pricings
    """
    plan_name = models.CharField(max_length=256)
    paper_type = models.CharField(max_length=256, null=True)
    price_per_sheet = models.IntegerField(null=True)
    discount = models.TextField(null=True, blank=True)
    # price = models.IntegerField(null=True)
    objects = PricingManager()

    def __str__(self):
        return self.plan_name


# class Grant(models.Model):
#     job = models.