from models import *
from google.appengine.api import users

class Seeder(object):

    def seed(self):

        self.user1 = User(
            email=users.User('1@gmail.com')
        )
        self.user1.put()
        self.user2 = User(
            email=users.User('2@gmail.com')
        )
        self.user2.put()
        self.post1 = Post(
            title='a',
            content='a',
            user=self.user1.key
        )
        self.post1.put()
        self.post2 = Post(
            title='b',
            content='b',
            user=self.user1.key
        )
        self.post2.put()
        self.post3 = Post(
            title='c',
            content='c',
            user=self.user2.key,
            parent=self.user2.key
        )
        self.post3.put()
        self.comment1 = Comment(
            content='d',
            post=self.post3.key,
            user=self.user2.key
        )
        self.comment1.put()
        self.comment2 = Comment(
            content='e',
            post=self.post3.key,
            user=self.user2.key
        )
        self.comment2.put()
        self.tag1 = Tag(
            name='f',
            post=self.post3.key,
            user=self.user2.key
        )
        self.tag1.put()
        self.tag2 = Tag(
            name='g',
            post=self.post3.key,
            user=self.user2.key
        )
        self.tag2.put()

    def clean(self):
        def __():
            for m in [
                User,
                Post,
                Tag,
                Comment
            ]:
                for e in m.query().fetch(1000):
                    yield e

        for k in __():
            k.key.delete()
