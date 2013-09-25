from google.appengine.api import users
from lib import HTTPError


def superuser(self, view, item):
    if not users.get_current_user() or not users.is_current_user_admin():
        raise HTTPError(403, 'log in')
    return

def owner(self, view, item):
    user = users.get_current_user()
    if not user or item.user != user:
        raise HTTPError(403, 'log in')
    return

def anyone(self, view, item):
    return

def none(self, view, item):
    raise HTTPError(403)
