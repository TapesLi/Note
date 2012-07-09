from core.models import Note
import utils
from django.http import HttpResponseRedirect, HttpResponse
from django.template import RequestContext
from django.utils import simplejson
from django.db import IntegrityError
from django.core.urlresolvers import reverse
from django.core import serializers
from django.shortcuts import render_to_response, get_object_or_404
from django.views.decorators.csrf import csrf_exempt
from datetime import datetime

def index(request):
    while True:
        note_url = utils.create_url();
        if not Note.objects.filter(url=note_url).exists():
            break
    return HttpResponseRedirect(reverse('core.views.note_detail', args=(note_url,)))

@csrf_exempt
def note_save(request): 
    url = request.POST.get('url', None)
    content = request.REQUEST['content']

    try:
        note = Note.objects.get(url=url)
        note.content  = content
        note.time = datetime.now()
    except Note.DoesNotExist:
        note = Note(content=content, time=datetime.now(), url=url) 

    try:
        note.save()
        note_json = serializers.serialize('json', [note,])[1:-1]
        return HttpResponse(note_json, mimetype='application/json')
    except IntegrityError:
        return HttpResponse(simplejson.dumps({'result': 'failed'}), mimetype='application/json')

def note_detail(request, note_url):
    context = {'url': note_url}
    try:
        note = Note.objects.get(url=note_url)
        context['note'] = note
    except Note.DoesNotExist:
        pass
    return render_to_response('core/note_detail.html',
            context,
            context_instance=RequestContext(request)
        )

def note_delete(request, note_url):
    try:
        note = Note.objects.get(url=note_url)
        note.delete()
        result = 'success'
    except:
        result = 'failed'
    return HttpResponse(simplejson.dumps({'result': result}), mimetype='application/json')

def notes_list(request):
    type = request.GET.get('type', None)
    notes = Note.objects.all().order_by('-time')

    if type == 'json':
        notes_json = serializers.serialize('json', notes )
        return HttpResponse(notes_json, mimetype='application/json') 
    else:
        return render_to_response('core/notes_list.html', {
            'notes': notes,
        },  context_instance=RequestContext(request))

