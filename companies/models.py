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


class ProposalForm(models.Model):
    name = models.CharField(max_length=255)
    plans = models.ManyToManyField(Plan)

    def __unicode__(self):
        return '%s from %s' % (self.name, self.plans.first().company)

    def __str__(self):
        return '%s from %s' % (self.name, self.plans.first().company)


class ProposalFormField(models.Model):
    proposal_form = models.ForeignKey(ProposalForm)
    title = models.CharField(max_length=255)
    required = models.BooleanField(default=True)
    field_type = models.CharField(max_length=255, choices=(
        ('boolean', 'Boolean'),
        ('text', 'Text'),
        ('float', 'Float'),
        ('file', 'File'),
    ))

    def __unicode__(self):
        return '%s in "%s"' % (self.title, self.proposal_form)

    def __str__(self):
        return '%s in "%s"' % (self.title, self.proposal_form)
