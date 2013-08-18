from google.appengine.api import users

def superuser(self, view, item):
    if not users.get_current_user() or not users.is_current_user_admin():
        view.response.set_status(403, 'log in')
        return 403
    return

def owner(self, view, item):
    user = users.get_current_user()
    if not user or item.user != user:
        return 403
    return

def anyone(self, view, item):
    return

def none(self, view, item):
    return 403
