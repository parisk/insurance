# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-10-01 10:26
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('companies', '0007_remove_proposalformfield_value'),
        ('clients', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProposalFormSubmission',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('submitted_on', models.DateTimeField(auto_now_add=True)),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='clients.Client')),
                ('proposal_form', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='companies.ProposalForm')),
            ],
        ),
        migrations.CreateModel(
            name='ProposalFormSubmissionField',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.CharField(max_length=65535)),
                ('field', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='companies.ProposalFormField')),
                ('proposal_form_submission', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='clients.ProposalFormSubmission')),
            ],
        ),
    ]
