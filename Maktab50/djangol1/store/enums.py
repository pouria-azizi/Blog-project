from django.db import models
from django.utils.translation import ugettext as _


class OrderStatuses(models.TextChoices):
    """
    Status an order can have
    """
    CREATED = 'CREATED', _('Created')
    COMPETED = 'COMPETED', _('Completed')
    CANCELED = 'CANCELED', _('Canceled')
    SUSPENDED = 'SUSPENDED', _('Suspended')
