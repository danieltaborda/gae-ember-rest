from google.appengine.ext import ndb
from lib import HTTPError


class Model(ndb.Model):
    date_created = ndb.DateTimeProperty(
        auto_now_add=True
    )
    date_updated = ndb.DateTimeProperty(
        auto_now_add=True
    )


class User(Model):
    email = ndb.UserProperty(
    )


class Post(Model):
    title = ndb.StringProperty(
    )
    content = ndb.TextProperty(
    )
    image = ndb.BlobProperty(
    )
    user = ndb.KeyProperty(
        kind=User
    )


class Tag(Model):
    name = ndb.StringProperty(
    )
    post = ndb.KeyProperty(
        kind=Post
    )
    user = ndb.KeyProperty(
        kind=User
    )


class Comment(Model):
    content = ndb.TextProperty(
    )
    post = ndb.KeyProperty(
        kind=Post
    )
    user = ndb.KeyProperty(
        kind=User
    )


class Error(Model):
    content = ndb.TextProperty(
    )
    def _pre_put_hook(self):
        e = 'some error'
        raise Exception(e)

