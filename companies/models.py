from __future__ import unicode_literals

from django.db import models


class Company(models.Model):
    name = models.CharField(max_length=255)

    def __unicode__(self):
        return self.name

    def __str__(self):
        return self.name


class Sector(models.Model):
    name = models.CharField(max_length=255)

    def __unicode__(self):
        return self.name

    def __str__(self):
        return self.name


class Plan(models.Model):
    name = models.CharField(max_length=255)
    company = models.ForeignKey(Company)
    sector = models.ForeignKey(Sector)

    def __unicode__(self):
        return '%s from %s for %s' % (self.name, self.company, self.sector)

    def __str__(self):
        return '%s from %s for %s' % (self.name, self.company, self.sector)
