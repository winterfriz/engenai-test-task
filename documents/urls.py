from . import views
from django.urls import path

urlpatterns = [
    path('', views.document_list, name='document-list'),
    path('search', views.document_list_search, name='document-list-search'),
    path('create', views.document_create, name='document-create'),
    path('update/<int:id>', views.document_update, name='document-update'),
    path('delete/<int:id>', views.document_delete, name='document-delete'),
]
