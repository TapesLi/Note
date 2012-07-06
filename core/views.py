from core.models import Note
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django.shortcuts import render_to_response, get_object_or_404

def index(request):
    notes = Note.objects.all().order_by('-time')
    return render_to_response('core/index.html', {
        'notes': notes
    })

def note_create(request): 
    content = request.POSt['content']
    time = request.POST['time']
    note = Note(content, time)
    note.save()
    return HttpResponseRedirect(reverse('core.views.note_detail', args=(note.id,)))

def note_detail(request, note_id):
    note = get_object_or_404(Note, pk=note_id)
    return render_to_response('core.note_detail.html', {
        'note': note,
    })

def note_update(request, note_id):
    note = get_object_or_404(Note, pk=note_id)
    note.content = request.POST['content']
    note.time = request.POST['time']
    note.save()

def note_delete(request, note_id):
    note = get_object_or_404(Note, pk=note_id)
    note.delete()
