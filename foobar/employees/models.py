from django.db import models
from django.utils.translation import ugettext_lazy as _


GENDER_CHOICES = (
    # (None, 'Gender'),
    ('F', 'Female'),
    ('M', 'Male'),
)

class Employee(models.Model):
    first_name = models.CharField(max_length=255, default='',
                                  blank=True, null=True,
                                  verbose_name=_('First Name'))

    last_name = models.CharField(max_length=255, default='',
                                 blank=True, null=True,
                                 verbose_name=_('Last Name'))

    # class Meta:
    #     app_label = 'proj2'

    # def __str__(self):
    #     if len(self.full_name()) > 5:
    #         return '{0} - {1}'.format(self.company, self.full_name())
    #     return '{0} - {1}'.format(self.company, self.serial)

    # class Meta:
    #     ordering = ['-last_updated']
