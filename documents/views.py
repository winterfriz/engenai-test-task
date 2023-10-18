from django.shortcuts import render, redirect
from .models import Document
from .forms import DocumentForm
from .service import create_embedding, search_documents


# Create your views here.
def document_list(request):
    documents = Document.objects.all()
    return render(request,"documents/document-list.html", {'documents': documents})


def document_list_search(request):
    search_query = request.GET.get('q', '')
    docs = search_documents(search_query)
    return render(request,"documents/document-list.html", {'documents': docs})


def document_create(request):
    if request.method == "POST":
        form = DocumentForm(request.POST)
        if form.is_valid():
            form.save()
            document = form.instance
            create_embedding(document)
            return redirect('document-list')
    else:
        form = DocumentForm()
    return render(request,'documents/document-create.html', {'form': form})


def document_update(request, id):
    document = Document.objects.get(id=id)
    form = DocumentForm(initial={'title': document.title, 'description': document.description,})
    if request.method == "POST":
        form = DocumentForm(request.POST, instance=document)
        if form.is_valid():
            try:
                form.save()
                return redirect('document-list')
            except Exception as e:
                pass
    return render(request,'documents/document-update.html',{'form':form})


def document_delete(request, id):
    document = Document.objects.get(id=id)
    try:
        document.delete()
    except:
        pass
    return redirect('document-list')
