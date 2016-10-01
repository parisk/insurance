from django.shortcuts import redirect
from django.shortcuts import render

from django.http import HttpResponse

from clients.models import Client
from clients.models import ProposalFormSubmission
from clients.models import ProposalFormSubmissionField
from companies.models import ProposalForm
from companies.models import ProposalFormField


def display_proposal_form(request, proposal_form_id):
    if request.method == 'POST':
        client = Client.objects.get(id=int(request.POST['client']))
        proposal_form = ProposalForm.objects.get(id=proposal_form_id)
        submission = ProposalFormSubmission.objects.create(
            client=client,
            proposal_form=proposal_form
        )
        fields = ProposalFormField.objects.filter(
            proposal_form=proposal_form
        )
        for field in fields:
            ProposalFormSubmissionField.objects.create(
                proposal_form_submission=submission,
                field=field,
                value=request.POST['%s' % field.id]
            )
        response = redirect(
            display_proposal_form_submission, submission_id=submission.id
        )
        return response
    else:
        proposal_form = ProposalForm.objects.get(id=proposal_form_id)
        data = {
            'proposal_form': proposal_form,
            'fields': ProposalFormField.objects.filter(
                proposal_form=proposal_form
            ),
            'clients': Client.objects.all()
        }
        return render(request, 'brokers/proposal_form.html', data)

def display_proposal_form_submission(request, submission_id):
    submission = ProposalFormSubmission.objects.get(id=submission_id)
    data = {
        'proposal_form_submission': submission,
        'fields': ProposalFormSubmissionField.objects.filter(
            proposal_form_submission=submission
        )
    }
    return render(request, 'brokers/proposal_form_submission.html', data)
