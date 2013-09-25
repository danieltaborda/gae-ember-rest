from google.appengine.api import users
from lib import Api, Apis
from models import *
import allow


class TagApi(Api):
    model = Tag
    fields = (
        'name',
        'post',
        'user',
    )
    __is_creatable__ = allow.owner
    __is_readable__ = allow.anyone
    __is_updatable__ = allow.owner
    __is_removable__ = allow.superuser


class UserApi(Api):
    model = User
    fields = (
        'email',
    )

    __is_creatable__ = allow.none
    __is_readable__ = allow.anyone
    __is_updatable__ = allow.none
    __is_removable__ = allow.superuser

class PostApi(Api):
    model = Post
    fields = (
        'title',
        'content',
        'user',
        'image'
    )

    __is_creatable__ = allow.superuser
    __is_readable__ = allow.anyone
    __is_updatable__ = allow.superuser
    __is_removable__ = allow.superuser

class CommentApi(Api):
    model = Comment
    fields = (
        'content',
        'post',
        'user',
    )

    __is_creatable__ = allow.owner
    __is_readable__ = allow.anyone
    __is_updatable__ = allow.owner
    __is_removable__ = allow.superuser


class ErrorApi(Api):
    model = Error
    fields = (
        'content',
    )
    __is_creatable__ = allow.anyone
    __is_readable__ = allow.anyone
    __is_updatable__ = allow.anyone
    __is_removable__ = allow.anyone


urls = Apis(
    TagApi,
    UserApi,
    PostApi,
    CommentApi,
    ErrorApi
)