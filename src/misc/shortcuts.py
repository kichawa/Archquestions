from google.appengine.api import users
from google.appengine.ext import db

from django.template import RequestContext
from django.shortcuts import render_to_response, redirect
from django.http import Http404


def render(request, template, context):
    """Available in django 1.3

    http://docs.djangoproject.com/en/dev/topics/http/shortcuts/
    """
    ctx = RequestContext(request, context)
    return render_to_response(template, ctx)

def login_required(view):
    """If user is not logger, redirect to login page
    """
    def decorator(request, *args, **kwargs):
        if users.get_current_user() is None:
            return redirect(users.create_login_url(request.path))
        return view(request, *args, **kwargs)

    return decorator

def get_object_or_404(model, key=None, key_name=None):
    """Get given model instance or raise Http404 exception
    """
    ins = None

    if key_name and key is None:
        key = db.Key.from_path(model.kind(), key_name)

    if key:
        # catch KindError here?
        ins = model.get(key)

    if ins is not None:
        return ins
    raise Http404
