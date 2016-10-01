from django.contrib import admin

from companies.models import Company
from companies.models import Plan
from companies.models import ProposalForm
from companies.models import ProposalFormField
from companies.models import Sector


class CompanyAdmin(admin.ModelAdmin):
    pass
admin.site.register(Company, CompanyAdmin)


class SectorAdmin(admin.ModelAdmin):
    pass
admin.site.register(Sector, SectorAdmin)


class PlanAdmin(admin.ModelAdmin):
    pass
admin.site.register(Plan, PlanAdmin)


class ProposalFormAdmin(admin.ModelAdmin):
    pass
admin.site.register(ProposalForm, ProposalFormAdmin)


class ProposalFormFieldAdmin(admin.ModelAdmin):
    pass
admin.site.register(ProposalFormField, ProposalFormFieldAdmin)
