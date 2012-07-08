from core.models import Note
import utils
from django.http import HttpResponseRedirect, HttpResponse
from django.template import RequestContext
from django.db import IntegrityError
from django.core.urlresolvers import reverse
from django.core import serializers
from django.shortcuts import render_to_response, get_object_or_404
from django.views.decorators.csrf import csrf_exempt
from datetime import datetime

def index(request):
    url = utils.create_url();
    return HttpResponseRedirect(reverse('core.views.note_detail', args=(url,)))

@csrf_exempt
def note_create(request): 
    content = request.REQUEST['content']
    time = datetime.now() 
    url = utils.create_url()
    note = Note(content=content, time=time, url=url)
    try:
        note.save()
        note_json = serializers.serialize('json', [note,])[1:-1]
        return HttpResponse(note_json, mimetype="application/json")
    except IntegrityError:
        pass

def note_detail(request, note_url):
    try:
        note = Note.objects.get(url=note_url)
        return render_to_response('core/note_detail.html', {
            'note': note,
            'url': note_url, 
        },  context_instance=RequestContext(request))
    except Note.DoesNotExist:
        return render_to_response('core/note_detail.html', {
            'url': note_url, 
        },  context_instance=RequestContext(request))
    

def note_update(request, note_id):
    note = get_object_or_404(Note, pk=note_id)
    note.content = request.POST['content']
    note.time = request.POST['time']
    note.save()

def note_delete(request, note_id):
    note = get_object_or_404(Note, pk=note_id)
    note.delete()

def notes_list(request):
    notes_json = serializers.serialize('json',  Note.objects.all().order_by('-time'))
    return HttpResponse(notes_json, mimetype="application/json") 

