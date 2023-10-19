from django.db import models
from pgvector.django import VectorField

from documents import consts


class Document(models.Model):
    # Define status choices as tuples
    PROCESSED = 'processed'
    NON_PROCESSED = 'non_processed'
    COMPLETED = 'completed'

    STATUS_CHOICES = [
        (PROCESSED, 'Processed'),
        (NON_PROCESSED, 'Non Processed'),
        (COMPLETED, 'Completed'),
    ]

    title = models.CharField(db_column='title', max_length=100)
    description = models.TextField(db_column='description', max_length=1000, blank=False)
    embedding = VectorField(dimensions=consts.DIMENSIONS, null=True,)
    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default=NON_PROCESSED,
    )
    last_search_date = models.DateTimeField(default=None, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class SearchQuery(models.Model):
    query = models.CharField(max_length=1000,)
    embedding = VectorField(dimensions=consts.DIMENSIONS, null=True,)
    created_at = models.DateTimeField(auto_now_add=True)



