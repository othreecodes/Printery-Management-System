from django.db import models

from django.contrib.auth.models import AbstractUser
from django.utils.translation import ugettext_lazy as _
from model_utils.models import TimeStampedModel
# from django_dropbox import storage


class User(AbstractUser):
    """
    User Model
    """
    name = models.CharField(_('Name of User'), blank=True, max_length=255)

    def __str__(self):
        return self.username


class Client(User):
    """
    Model for all clients
    """
    class Meta:
        verbose_name = 'Client'
        verbose_name_plural = 'Clients'


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
    charged_to = models.ForeignKey(Client)
    printer = models.CharField(max_length=256)
    copies = models.IntegerField()
    cost = models.IntegerField()
    status_choices = (("Started", "Started"), ("Pending",
                                               "Pending"), ("Completed", "Completed"))
    status = models.CharField(choices=status_choices, max_length=256)
    document = models.ForeignKey(Document)

    def __str__(self):
        return self.charged_to + " - " + self.document
