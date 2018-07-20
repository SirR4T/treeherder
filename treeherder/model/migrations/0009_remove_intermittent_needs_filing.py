# -*- coding: utf-8 -*-
# Generated by Django 1.11.14 on 2018-07-20 08:28
from __future__ import unicode_literals

from django.db import migrations

NEEDS_FILING = "intermittent needs filing"


def remove_job_notes(apps, schema_editor):
    JobNote = apps.get_model("model", "JobNote")

    JobNote.objects.filter(failure_classification__name=NEEDS_FILING).delete()


def set_jobs_to_unclassified(apps, schema_editor):
    Job = apps.get_model("model", "Job")
    (Job.objects.filter(failure_classification__name=NEEDS_FILING)
                .update(failure_classification_id=1))


def remove_intermittent_needs_filing(apps, schema_editor):
    FailureClassification = apps.get_model("model", "FailureClassification")
    FailureClassification.objects.get(name=NEEDS_FILING).delete()


def add_intermittent_needs_filing(apps, schema_editor):
    FailureClassification = apps.get_model("model", "FailureClassification")
    FailureClassification.objects.create(
        id=6,
        name=NEEDS_FILING,
    )


class Migration(migrations.Migration):

    dependencies = [
        ('model', '0008_remove_failure_match'),
    ]

    operations = [
        migrations.RunPython(remove_job_notes),
        migrations.RunPython(set_jobs_to_unclassified),
        migrations.RunPython(remove_intermittent_needs_filing, reverse_code=add_intermittent_needs_filing)
    ]
