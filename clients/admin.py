from django.contrib import admin

from clients.models import Client
from clients.models import ProposalFormSubmission
from clients.models import ProposalFormSubmissionField


class ClientAdmin(admin.ModelAdmin):
    pass
admin.site.register(Client, ClientAdmin)


class ProposalFormSubmissionAdmin(admin.ModelAdmin):
    pass
admin.site.register(ProposalFormSubmission, ProposalFormSubmissionAdmin)


class ProposalFormSubmissionFieldAdmin(admin.ModelAdmin):
    pass
admin.site.register(
    ProposalFormSubmissionField, ProposalFormSubmissionFieldAdmin
)
