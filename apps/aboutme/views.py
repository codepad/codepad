from django.core.urlresolvers import reverse
from django.shortcuts import render_to_response
from django.template.loader import get_template
from django.template.context import RequestContext
from django.template import Context, loader, Template
from django.contrib.auth.decorators import login_required
from django.forms.formsets import formset_factory, BaseFormSet
from django.http import HttpResponse, Http404, HttpResponseRedirect,\
    HttpResponseNotAllowed
from django.conf import settings



# Create your views here.
# TO DO:Please user decorator for login
def aboutme(request):
    context = RequestContext(request)
    return render_to_response('resume.html', context_instance=context)
