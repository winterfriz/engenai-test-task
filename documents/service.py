import logging

import openai
from django.forms import model_to_dict
from openai.embeddings_utils import get_embedding, cosine_similarity

from documents import consts
from documents.models import Document

logger = logging.getLogger(__name__)


def create_embedding(document: Document) -> None:
    """
    Create embedding using OpenAI API and store it
    to document instance that will be marked as 'processed'

    Args:
        document (Document): instance of Document model

    Returns:
        None
    """
    try:
        response = openai.Embedding.create(input=document.description, model=consts.EMBEDDING_MODEL)
        embedding = response['data'][0]['embedding']

        document.embedding = embedding
        document.status = Document.PROCESSED
        document.save(update_fields=['embedding', 'status'])

    except openai.error.OpenAIError as e:
        logger.error(f"An OpenAI error occurred while creating an embedding for document {document.id}: {e}")


def search_documents(search: str) -> list[dict]:
    """
    Search documents which contain search query.
    Cosine similarity mechanism is used for retrieving relevant documents.

    Args:
        search (str): The search query.

    Returns:
        list of dicts: A list of document data dictionaries sorted by similarity.
    """
    search_embedding = get_embedding(search, engine=consts.EMBEDDING_MODEL)
    documents = Document.objects.filter(status=Document.PROCESSED)
    data_dicts = [model_to_dict(instance) for instance in documents]

    for doc in data_dicts:
        doc['similarity'] = cosine_similarity(doc['embedding'], search_embedding)

    sorted_data_desc = sorted(data_dicts, key=lambda x: x['similarity'], reverse=True)
    return sorted_data_desc
