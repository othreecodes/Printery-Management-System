from django.db import models

from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import ugettext_lazy as _
from model_utils.models import TimeStampedModel


class User(AbstractUser):
    name = models.CharField(_('Name of User'), blank=True, max_length=255)

    def __str__(self):
        return self.username


class Client(User):
    pass


class Document(models.Model):
    pass


class PrintJob(TimeStampedModel):
    charged_to = models.ForeignKey(Client)
    printer = models.CharField(max_length=256)
    copies = models.IntegerField()
    cost = models.IntegerField()
    status = models.CharField()
    document = models.ForeignKey(Document)
