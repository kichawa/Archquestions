from google.appengine.api import users


def user(request):
    """Put user object into context. If user is not logger, push `None` instead
    """
    return {'user': users.get_current_user()}
