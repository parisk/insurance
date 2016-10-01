from __future__ import unicode_literals

from django.db import models

from companies.models import ProposalForm
from companies.models import ProposalFormField


class Client(models.Model):
    name = models.CharField(max_length=255)

    def __unicode__(self):
        return self.name

    def __str__(self):
        return self.name


class ProposalFormSubmission(models.Model):
    client = models.ForeignKey(Client)
    proposal_form = models.ForeignKey(ProposalForm)
    submitted_on = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return '%s submission of "%s"' % (self.client, self.proposal_form)

    def __str__(self):
        return '%s submission of "%s"' % (self.client, self.proposal_form)


class ProposalFormSubmissionField(models.Model):
    proposal_form_submission = models.ForeignKey(ProposalFormSubmission)
    field = models.ForeignKey(ProposalFormField)
    value = models.CharField(max_length=65535)
