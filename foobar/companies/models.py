from django.db import models
from django.utils.translation import ugettext_lazy as _
from django_countries.fields import CountryField


class Company(models.Model):
    """Definition of Company Model."""

    name = models.CharField(max_length=255, blank=False,
                            verbose_name=_('Name'))
    slug = models.SlugField(unique=True, blank=True, max_length=255)

    country = CountryField(blank=True, null=True, help_text=_('Company country'), blank_label=_('Select country'))
    region = models.CharField(max_length=60, blank=True, null=True,
                              help_text=_('Region'))
    city = models.CharField(max_length=60, blank=True, null=True,
                            help_text=_('City'))
    address = models.CharField(max_length=60, blank=True, null=True,
                               help_text=_('Address'))

    def __str__(self):
        # return 'Company: {0}'.format(self.name)
        return self.name

    class Meta:
        # app_label = 'common'
        verbose_name_plural = _('companies')
        ordering = ['id']
